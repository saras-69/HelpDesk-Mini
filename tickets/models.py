from django.db import models
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
import uuid

class Ticket(models.Model):
    """
    Main ticket model with SLA tracking and optimistic locking
    """
    STATUS_CHOICES = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]
    
    # Basic fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    
    # User relationships
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='created_tickets'
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='assigned_tickets'
    )
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # SLA tracking
    sla_due_date = models.DateTimeField(null=True, blank=True)
    is_sla_breached = models.BooleanField(default=False)
    
    # Optimistic locking
    version = models.IntegerField(default=1)
    
    def save(self, *args, **kwargs):
        # Check if this is a new instance (either no pk or created_at is None)
        is_new = self.pk is None or self.created_at is None
        
        # Calculate SLA due date for new tickets
        if is_new and not self.sla_due_date and self.status == 'open':
            hours_map = {
                'critical': 4,
                'high': 24,
                'medium': 72,
                'low': 168,  # 1 week
            }
            # Use timezone.now() as the base time for new tickets
            self.sla_due_date = timezone.now() + timedelta(hours=hours_map[self.priority])
        
        # Check SLA breach
        if self.sla_due_date and timezone.now() > self.sla_due_date and self.status not in ['resolved', 'closed']:
            self.is_sla_breached = True
        
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"#{self.id} - {self.title}"
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['priority']),
            models.Index(fields=['created_by']),
            models.Index(fields=['assigned_to']),
            models.Index(fields=['is_sla_breached']),
        ]

class Comment(models.Model):
    """
    Threaded comments for tickets
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.author.username} on {self.ticket.title}"
    
    class Meta:
        ordering = ['created_at']

class Timeline(models.Model):
    """
    Timeline/audit log for ticket actions
    """
    ACTION_CHOICES = [
        ('created', 'Ticket Created'),
        ('updated', 'Ticket Updated'),
        ('status_changed', 'Status Changed'),
        ('assigned', 'Ticket Assigned'),
        ('commented', 'Comment Added'),
        ('priority_changed', 'Priority Changed'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='timeline')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    description = models.TextField()
    metadata = models.JSONField(default=dict, blank=True)  # Store additional data
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.action} - {self.ticket.title} by {self.user.username}"
    
    class Meta:
        ordering = ['-created_at']

class SLAConfiguration(models.Model):
    """
    SLA configuration for different priorities
    """
    priority = models.CharField(max_length=10, choices=Ticket.PRIORITY_CHOICES, unique=True)
    response_hours = models.IntegerField(help_text="Hours for initial response")
    resolution_hours = models.IntegerField(help_text="Hours for resolution")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"SLA for {self.get_priority_display()}"
    
    class Meta:
        verbose_name = "SLA Configuration"
        verbose_name_plural = "SLA Configurations"
