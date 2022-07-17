from django.forms import ModelForm
from .models import Room
from django import forms
from accounts.models import SpecialUser
from django.shortcuts import get_object_or_404, redirect, render


class RoomCreateForm(ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description']


class RoomUpdateForm(ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description']
