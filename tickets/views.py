from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Ticket, Comment, Timeline

@login_required
def ticket_list(request):
    """List all tickets with filtering and pagination"""
    tickets = Ticket.objects.all()
    
    # Search functionality
    search = request.GET.get('search')
    if search:
        tickets = tickets.filter(
            Q(title__icontains=search) |
            Q(description__icontains=search) |
            Q(comments__content__icontains=search)
        ).distinct()
    
    # Filter by status
    status = request.GET.get('status')
    if status:
        tickets = tickets.filter(status=status)
    
    # Filter by priority
    priority = request.GET.get('priority')
    if priority:
        tickets = tickets.filter(priority=priority)
    
    # Pagination
    paginator = Paginator(tickets, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search': search,
        'status': status,
        'priority': priority,
        'status_choices': Ticket.STATUS_CHOICES,
        'priority_choices': Ticket.PRIORITY_CHOICES,
    }
    return render(request, 'tickets/ticket_list.html', context)

@login_required
def ticket_detail(request, pk):
    """Display ticket details with comments"""
    ticket = get_object_or_404(Ticket, pk=pk)
    comments = ticket.comments.filter(parent=None).order_by('created_at')
    timeline = ticket.timeline.all()[:10]  # Latest 10 timeline entries
    
    context = {
        'ticket': ticket,
        'comments': comments,
        'timeline': timeline,
    }
    return render(request, 'tickets/ticket_detail.html', context)

@login_required
def ticket_create(request):
    """Create a new ticket"""
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority', 'medium')
        
        if title and description:
            ticket = Ticket.objects.create(
                title=title,
                description=description,
                priority=priority,
                created_by=request.user
            )
            
            # Create timeline entry
            Timeline.objects.create(
                ticket=ticket,
                user=request.user,
                action='created',
                description=f'Ticket created with priority {ticket.get_priority_display()}'
            )
            
            messages.success(request, 'Ticket created successfully!')
            return redirect('ticket_detail', pk=ticket.pk)
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    return render(request, 'tickets/ticket_create.html', {
        'priority_choices': Ticket.PRIORITY_CHOICES
    })
