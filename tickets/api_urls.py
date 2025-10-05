from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register(r'tickets', api_views.TicketViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('tickets/<uuid:ticket_id>/comments/', api_views.CommentListCreateView.as_view(), name='ticket-comments'),
]