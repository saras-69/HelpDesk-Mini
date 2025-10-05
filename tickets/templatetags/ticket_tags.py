from django import template

register = template.Library()

@register.filter
def status_badge_class(status):
    """Convert ticket status to appropriate CSS badge class"""
    status_map = {
        'open': 'badge-open',
        'in_progress': 'badge-in-progress', 
        'resolved': 'badge-resolved',
        'closed': 'badge-closed'
    }
    return status_map.get(status, 'badge-open')

@register.filter  
def priority_class(priority):
    """Convert ticket priority to appropriate CSS class"""
    return f"priority-{priority}"