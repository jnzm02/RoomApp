from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    path('<str:title>/edit', login_required(views.room_update_view), name='room_edit'),
    path('create/', login_required(views.room_create_view), name='room_create'),
    path('<str:title>/', views.room_detail_view, name='room_detail'),
    path('', login_required(views.room_list_view), name='room_list'),
    path('<str:title>/delete', login_required(views.room_delete_view), name='room_delete')
]
