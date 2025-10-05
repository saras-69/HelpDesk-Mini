from django.contrib import admin
from .models import Ticket, Comment, Timeline, SLAConfiguration

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['title', 'status', 'priority', 'created_by', 'assigned_to', 'is_sla_breached', 'created_at']
    list_filter = ['status', 'priority', 'is_sla_breached', 'created_at']
    search_fields = ['title', 'description', 'created_by__username']
    readonly_fields = ['version', 'created_at', 'updated_at', 'is_sla_breached']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'status', 'priority')
        }),
        ('Assignment', {
            'fields': ('created_by', 'assigned_to')
        }),
        ('SLA Tracking', {
            'fields': ('sla_due_date', 'is_sla_breached')
        }),
        ('System Fields', {
            'fields': ('version', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'author', 'content_preview', 'parent', 'created_at']
    list_filter = ['created_at', 'author']
    search_fields = ['content', 'ticket__title', 'author__username']
    
    def content_preview(self, obj):
        return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content
    content_preview.short_description = 'Content Preview'

@admin.register(Timeline)
class TimelineAdmin(admin.ModelAdmin):
    list_display = ['ticket', 'user', 'action', 'description', 'created_at']
    list_filter = ['action', 'created_at']
    readonly_fields = ['created_at']
    search_fields = ['ticket__title', 'user__username', 'description']

@admin.register(SLAConfiguration)
class SLAConfigurationAdmin(admin.ModelAdmin):
    list_display = ['priority', 'response_hours', 'resolution_hours', 'updated_at']
    list_editable = ['response_hours', 'resolution_hours']
