from django.urls import path
from .views import (
    RoomsListView, 
    RoomCreateView,
    RoomDeleteView, 
    RoomDetailView,
    RoomUpdateView,
    RoomEnterView
)

urlpatterns = [
    path('', RoomsListView.as_view(), name = 'room_list'),
    path('create/', RoomCreateView.as_view(), name = 'room_create'),
    path('<int:pk>/edit', RoomUpdateView.as_view(), name = 'room_edit'),
    path('<int:pk>/', RoomDetailView.as_view(), name = 'room_detail'),
    path('<int:pk>/delete', RoomDeleteView.as_view(), name = 'room_delete'),
    path('<int:pk>/enter', RoomEnterView.as_view(), name='room_enter'),
]