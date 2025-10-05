from rest_framework import viewsets, status, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Ticket, Comment, Timeline
from .serializers import TicketSerializer, CommentSerializer, TimelineSerializer

class TicketViewSet(viewsets.ModelViewSet):
    """
    ViewSet for Ticket CRUD operations with optimistic locking
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Search functionality
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(description__icontains=search) |
                Q(comments__content__icontains=search)
            ).distinct()
        
        # Filter by status
        status_filter = self.request.query_params.get('status')
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        # Filter by priority
        priority = self.request.query_params.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)
        
        # Filter by assigned user
        assigned_to = self.request.query_params.get('assigned_to')
        if assigned_to:
            queryset = queryset.filter(assigned_to_id=assigned_to)
        
        return queryset.order_by('-created_at')
    
    def perform_create(self, serializer):
        ticket = serializer.save(created_by=self.request.user)
        
        # Create timeline entry
        Timeline.objects.create(
            ticket=ticket,
            user=self.request.user,
            action='created',
            description=f'Ticket created with priority {ticket.get_priority_display()}'
        )
    
    def perform_update(self, serializer):
        # Get the current version from request
        version = self.request.data.get('version')
        instance = self.get_object()
        
        # Optimistic locking check
        if version and int(version) != instance.version:
            return Response(
                {'error': 'Ticket has been modified by another user. Please refresh and try again.'},
                status=status.HTTP_409_CONFLICT
            )
        
        # Store original values for timeline
        original_status = instance.status
        original_priority = instance.priority
        original_assigned_to = instance.assigned_to
        
        # Update the ticket and increment version
        ticket = serializer.save(version=instance.version + 1)
        
        # Create timeline entries for changes
        changes = []
        if original_status != ticket.status:
            changes.append(f'Status changed from {original_status} to {ticket.status}')
            Timeline.objects.create(
                ticket=ticket,
                user=self.request.user,
                action='status_changed',
                description=f'Status changed from {original_status} to {ticket.status}',
                metadata={'from': original_status, 'to': ticket.status}
            )
        
        if original_priority != ticket.priority:
            changes.append(f'Priority changed from {original_priority} to {ticket.priority}')
            Timeline.objects.create(
                ticket=ticket,
                user=self.request.user,
                action='priority_changed',
                description=f'Priority changed from {original_priority} to {ticket.priority}',
                metadata={'from': original_priority, 'to': ticket.priority}
            )
        
        if original_assigned_to != ticket.assigned_to:
            old_user = original_assigned_to.username if original_assigned_to else 'Unassigned'
            new_user = ticket.assigned_to.username if ticket.assigned_to else 'Unassigned'
            Timeline.objects.create(
                ticket=ticket,
                user=self.request.user,
                action='assigned',
                description=f'Assigned to {new_user}',
                metadata={'from': old_user, 'to': new_user}
            )
        
        if changes:
            Timeline.objects.create(
                ticket=ticket,
                user=self.request.user,
                action='updated',
                description='; '.join(changes)
            )
    
    @action(detail=True, methods=['get'])
    def timeline(self, request, pk=None):
        """Get ticket timeline"""
        ticket = self.get_object()
        timeline = ticket.timeline.all()
        serializer = TimelineSerializer(timeline, many=True)
        return Response(serializer.data)

class CommentListCreateView(generics.ListCreateAPIView):
    """
    API view for listing and creating comments on a ticket
    """
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        ticket_id = self.kwargs['ticket_id']
        return Comment.objects.filter(ticket_id=ticket_id, parent=None).order_by('created_at')
    
    def perform_create(self, serializer):
        ticket_id = self.kwargs['ticket_id']
        ticket = get_object_or_404(Ticket, id=ticket_id)
        
        comment = serializer.save(
            ticket=ticket,
            author=self.request.user
        )
        
        # Create timeline entry
        Timeline.objects.create(
            ticket=ticket,
            user=self.request.user,
            action='commented',
            description=f'Added comment: {comment.content[:50]}...' if len(comment.content) > 50 else f'Added comment: {comment.content}'
        )