from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# from .forms import RoomEnterForm
from .models import Room
from accounts.models import SpecialUser


class RoomsListView(ListView):
    model = Room
    template_name = 'rooms/room_list.html'


class RoomCreateView(LoginRequiredMixin, CreateView):
    model = Room
    fields = ('title', 'description', 'is_private')
    template_name = 'rooms/room_create.html'
    success_url = reverse_lazy('room_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class RoomDetailView(DetailView):
    model = Room
    template_name = 'rooms/room_detail.html'


class RoomUpdateView(LoginRequiredMixin, UpdateView):
    model = Room
    fields = ('title', 'creator', 'description', 'is_private')
    template_name = 'rooms/room_edit.html'

    def dispatch(self, request, *args, **kwargs):
        # it checks if the requesting user is creator of the current Room or superuser
        # in case if he is creator or superuser it allows user to change the Room

        """https://stackoverflow.com/questions/15424658/how-to-restrict-access-to-certain-user-to-an-updateview"""
        current_room = self.get_object()
        if current_room.creator == self.request.user or self.request.user.is_superuser:
            return super(UpdateView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404("You are not allowed to edit this Room")

    # TODO: Need to add password field for updating(highly recommended)


class RoomDeleteView(LoginRequiredMixin, DeleteView):
    model = Room
    template_name = 'rooms/room_delete.html'
    success_url = reverse_lazy('room_list')

    def dispatch(self, request, *args, **kwargs):
        # it checks if the requesting user is creator of the current Room or superuser
        # in case if he is creator or superuser it allows user to delete the Room

        current_room = self.get_object()
        if current_room.creator == self.request.user or self.request.user.is_superuser:
            return super(DeleteView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404("You are not allowed to delete this Room")


class RoomEnterView(LoginRequiredMixin, UpdateView):
    model = Room
    fields = ('entered_password',)
    template_name = 'rooms/room_enter.html'

    # needs to enter only members of the room who entered password correctly (still not finished) one of the answers
    # could be to add 2 password fields for Room model and one of them would be the password creator entered,
    # and another for entering for user (if matches he will have access to the room) (not sure if that works but hope)

    # if Room.password_entered == Room.room_password:
    #     success_url = reverse_lazy('room_details')
    # else:
    #     success_url = reverse_lazy('room_list')

    # We will change the password entered to '123' which is not acceptable for the password of the room in order to
    # change the password each time the user enters some password password_entered = '123'
