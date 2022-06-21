# from attr import fields
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

# one of the possible answers could be done via decorators (not sure, but hope)
# from tools.decorators import creator_only

# from .forms import RoomEnterForm
from .models import Room


# Create your views here.
# https://towardsdatascience.com/create-a-django-app-with-login-restricted-pages-31229cc48791

class RoomsListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ('title', 'online_users', 'number_of_users',)# Private -> boolean, password value->string
    template_name = 'rooms/room_create.html'
    success_url = reverse_lazy('room_list')

    # create room as user who logged in
    # https://docs.djangoproject.com/en/4.0/topics/class-based-views/generic-editing/
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

    # Access only for creator or superuser (not finished, searching for answer, still not found)

    # def form_valid(self, form):
    #     if self.request.user == form.instance.creator:
    #         return super.form_valid(form)


# @creator_only
class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'rooms/room_delete.html'
    success_url = reverse_lazy('room_list')

    # Access only for creator or superuser (not finished, searching for answer, still not found)

    # def form_valid(self, form):
    #     if self.request.user == form.instance.creator:
    #         return super.form_valid(form)


class RoomEnterView(LoginRequiredMixin, UpdateView):
    model = Room
    fields = ('entered_password',)
    template_name = 'rooms/room_enter.html'

    # needs to enter only members of the room who entered password correctly (still not finished)
    # one of the answers could be to add 2 password fields for Room model and one of them would be the password creator entered, and another for entering for user (if matches he will have an access to the room) (not sure that works but hope)

    # if Room.password_entered == Room.room_password:
    #     success_url = reverse_lazy('room_details')
    # else:
    #     success_url = reverse_lazy('room_list')

    #We will change the password entered to '123' which is not acceptable for the password of the room in order to change the password each time the user enters some password
    # password_entered = '123'
