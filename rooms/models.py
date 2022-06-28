from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from accounts.models import SpecialUser


class Room(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='room_creator')
    is_private = models.BooleanField(default=False)
    password = models.CharField(max_length=32, blank=True)
    number_of_users = models.IntegerField(default=0, validators=[MaxValueValidator(800000000), MinValueValidator(0)])
    room_image = models.ImageField(upload_to='room_images', default="images/icon.jpg", blank=False, null=False)
    description = models.CharField(max_length=32, blank=True)

    # TODO: request to join room from Room creator via email message or the website itself using Room password
    # if request sent then, the user can not ask for another request because user was refused or still in waiting list

    # TODO: USERS LIST WHO ARE ALLOWED TO ENTER THE ROOM
    room_members = models.ManyToManyField(SpecialUser, related_name='room_member', default=creator)

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])
