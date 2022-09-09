import http.client

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, View
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponse
from django.shortcuts import render
from django import forms
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from .models import Room
from django import forms
from accounts.models import SpecialUser
from django.shortcuts import get_object_or_404, redirect, render
from .forms import RoomCreateForm, RoomUpdateForm
from .models import Room
from accounts.models import SpecialUser


def room_list_view(request):
    q = request.GET.get('q') if request.GET.get('q') is not None else ''

    rooms = Room.objects.filter(
        Q(title__icontains=q) |
        Q(creator__username__icontains=q) |
        Q(description__icontains=q)
    )
    user = request.user
    room_number = rooms.count()
    for room in rooms:
        for member in room.room_members.all():
            member.number_of_rooms = member.rooms.count()
            member.save()

    context = {'rooms': rooms, 'user': user, 'room_number': room_number}
    return render(request, 'rooms/room_list.html', context)


def room_create_view(request):
    form = RoomCreateForm
    if request.method == 'POST':
        title = request.POST.get('title')
        if Room.objects.filter(title=title).exists():
            messages.add_message(request, messages.ERROR,
                                 "Room with this title already exists, please choose another title")
            return render(request, 'rooms/room_create.html', {'messages': [messages]})
        else:
            Room.objects.create(
                creator=request.user,
                title=request.POST.get('title'),
                description=request.POST.get('description'),
            )
            room = Room.objects.get(title=title)
            room.room_members.add(request.user)
            room.number_of_users = 1
            room.save()
            return redirect('room_list')

    context = {'form': form}
    return render(request, 'rooms/room_create.html', context)


def room_detail_view(request, title):
    room = Room.objects.get(title=title)
    user = request.user
    if not room.room_members.filter(username=user.username).exists():
        room.room_members.add(user)
        room.number_of_users = room.room_members.count()
        room.save()
    context = {'room': room}
    return render(request, 'rooms/room_detail.html', context)


def room_update_view(request, title):
    room = Room.objects.get(title=title)
    form = RoomUpdateForm(instance=room)

    if request.user != room.creator and not request.user.is_superuser:
        return HttpResponse("You are not allowed to edit this room!")

    if request.method == 'POST':
        title = request.POST.get('title')
        if Room.objects.filter(title=title).exists() and room.title != title:
            messages.add_message(request, messages.ERROR,
                                 "The room with this title already exists, please choose another one")
            return render(request, 'rooms/room_edit.html', {'messages': [messages]})
        room.title = request.POST.get('title')
        room.description = request.POST.get('description')
        room.save()
        return redirect('room_detail', room.title)

    context = {'form': form, 'room': room}
    return render(request, 'rooms/room_edit.html', context)


def room_delete_view(request, title):
    room = Room.objects.get(title=title)
    if request.user != room.creator and not request.user.is_superuser:
        return HttpResponse("You are not allowed to delete this Room")
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'rooms/room_delete.html', {'room': room})
