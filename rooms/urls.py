from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (
    RoomsListView,
    RoomCreateView,
    RoomDeleteView,
    RoomDetailView,
    RoomUpdateView,
    RoomEnterView
)

from . import views

urlpatterns = [
    path('', login_required(RoomsListView.as_view()), name='room_list'),
    path('create/', login_required(RoomCreateView.as_view()), name='room_create'),
    path('<int:pk>/edit', login_required(RoomUpdateView.as_view()), name='room_edit'),
    path('<int:pk>/', login_required(RoomDetailView.as_view()), name='room_detail'),
    # path('<str:title>/', views.detail_view, name='room_detail'),
    path('<int:pk>/delete', login_required(RoomDeleteView.as_view()), name='room_delete'),
    path('<int:pk>/enter', login_required(RoomEnterView.as_view()), name='room_enter'),
]
