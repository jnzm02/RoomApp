from tabnanny import verbose
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.

class Room(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE
    )
    #validators like limiters, the number cannot exceed the given value
    online_users = models.IntegerField(default=0, validators=[MaxValueValidator(800000000), MinValueValidator(0)])
    number_of_users = models.IntegerField(default=0, validators=[MaxValueValidator(800000000), MinValueValidator(0)])
    
    # we need add to password because Rooms should be private
    # room_password = models.CharField(max_length=50, default = "345")
    # entered_password = models.CharField(max_length=50, default = "123")

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        # db_table = "Rooms"

    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])