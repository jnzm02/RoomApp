from django.contrib import admin
from .models import Room

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    model = Room

admin.site.register(Room, RoomAdmin)