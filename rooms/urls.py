from django.urls import path
from django.contrib.auth.decorators import login_required

# from .views import (
#     RoomsListView,
#     RoomCreateView,
#     RoomDeleteView,
#     RoomDetailView,
#     RoomUpdateView,
#     RoomEnterView
# )

from . import views

urlpatterns = [
    # path('', login_required(RoomsListView.as_view()), name='room_list'),
    # path('create/', login_required(RoomCreateView.as_view()), name='room_create'),
    # path('<int:pk>/edit', login_required(RoomUpdateView.as_view()), name='room_edit'),
    path('<str:title>/edit', login_required(views.room_update_view), name='room_edit'),
    # path('<int:pk>/', login_required(RoomDetailView.as_view()), name='room_detail'),
    path('create/', login_required(views.room_create_view), name='room_create'),
    path('<str:title>/', views.room_detail_view, name='room_detail'),
    path('', login_required(views.room_list_view), name='room_list'),
    path('<str:title>/delete', login_required(views.room_delete_view), name='room_delete')
    # path('<int:pk>/delete', login_required(RoomDeleteView.as_view()), name='room_delete'),
    # path('<int:pk>/enter', login_required(RoomEnterView.as_view()), name='room_enter'),
]
