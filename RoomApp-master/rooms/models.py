from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django import forms


# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    private = models.BooleanField(default=False) # TODO: This field aimed to put button (or kinda) for switch
    # (validators like limiters, the number cannot exceed the given value) we still did not update the total number of
    # people who is the member of the given room, so I just gave the default value till we fix it
    # FIXME: "online_users" should be implemented as value from backend, not from user configuration
    online_users = models.IntegerField(default=0, validators=[MaxValueValidator(800000000), MinValueValidator(0)])
    number_of_users = models.IntegerField(default=0, validators=[MaxValueValidator(800000000), MinValueValidator(0)])
    password = forms.CharField(widget=forms.PasswordInput)
    # we need add to password because Rooms should be private room password is the password which creator created for
    # room itself (we gave default_value 'naruto' for filling the rooms, which were existed till the updating the
    # model in the database

    # room_password = models.CharField(max_length=50, default = "Naruto")

    # entered password is for users to enter if this matches with the room_password we will give him access to the
    # room he/she entering (not sure that this method will work, but hope)

    # entered_password = models.CharField(max_length=50, default = "123")

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        # db_table = "Rooms"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])
