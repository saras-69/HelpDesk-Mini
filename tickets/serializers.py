from rest_framework import serializers
from .models import Ticket, Comment, Timeline
from accounts.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
        read_only_fields = ['id']

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    replies = serializers.SerializerMethodField()
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'author', 'parent', 'replies', 'created_at', 'updated_at']
        read_only_fields = ['id', 'author', 'created_at', 'updated_at']
    
    def get_replies(self, obj):
        if obj.replies.exists():
            return CommentSerializer(obj.replies.all(), many=True).data
        return []

class TimelineSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Timeline
        fields = ['id', 'action', 'description', 'metadata', 'user', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']

class TicketSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    assigned_to = UserSerializer(read_only=True)
    assigned_to_id = serializers.UUIDField(write_only=True, required=False, allow_null=True)
    comments_count = serializers.SerializerMethodField()
    latest_comment = serializers.SerializerMethodField()
    
    class Meta:
        model = Ticket
        fields = [
            'id', 'title', 'description', 'status', 'priority',
            'created_by', 'assigned_to', 'assigned_to_id',
            'created_at', 'updated_at', 'sla_due_date', 'is_sla_breached',
            'version', 'comments_count', 'latest_comment'
        ]
        read_only_fields = [
            'id', 'created_by', 'created_at', 'updated_at', 
            'is_sla_breached', 'comments_count', 'latest_comment'
        ]
    
    def get_comments_count(self, obj):
        return obj.comments.count()
    
    def get_latest_comment(self, obj):
        latest = obj.comments.order_by('-created_at').first()
        if latest:
            return {
                'content': latest.content[:100] + '...' if len(latest.content) > 100 else latest.content,
                'author': latest.author.username,
                'created_at': latest.created_at
            }
        return None
    
    def update(self, instance, validated_data):
        # Handle assigned_to_id
        assigned_to_id = validated_data.pop('assigned_to_id', None)
        if assigned_to_id is not None:
            if assigned_to_id == '':
                validated_data['assigned_to'] = None
            else:
                try:
                    assigned_user = User.objects.get(id=assigned_to_id)
                    validated_data['assigned_to'] = assigned_user
                except User.DoesNotExist:
                    raise serializers.ValidationError({'assigned_to_id': 'User not found'})
        
        return super().update(instance, validated_data)