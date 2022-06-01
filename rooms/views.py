from attr import fields
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# from .forms import RoomEnterForm
from .models import Room

# Create your views here.
#https://towardsdatascience.com/create-a-django-app-with-login-restricted-pages-31229cc48791

class RoomsListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'

class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ('title', 'online_users', 'number_of_users',)
    template_name = 'rooms/room_create.html'
    success_url = reverse_lazy('room_list')

    # create room as user who logged in
    #https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/        
    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'

class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    fields = ('title', 'creator')
    template_name = 'rooms/room_edit.html'  

class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'rooms/room_delete.html'
    success_url = reverse_lazy('room_list')

class RoomEnterView(LoginRequiredMixin, UpdateView):
    model = Room
    fields = ('entered_password',)
    template_name = 'room/room_enter.html'
    # if Room.password_entered == Room.room_password:
    #     success_url = reverse_lazy('room_details')
    # else:
    #     success_url = reverse_lazy('room_list')
    # password_entered = '123'