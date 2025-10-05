from django.urls import path
from django.shortcuts import redirect
from . import views

def redirect_to_tickets(request):
    return redirect('ticket_list')

urlpatterns = [
    path('', redirect_to_tickets, name='home'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/new/', views.ticket_create, name='ticket_create'),
    path('tickets/<uuid:pk>/', views.ticket_detail, name='ticket_detail'),
]