from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator


class Room(models.Model):
    title = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_private = models.BooleanField(default=False)
    password = models.CharField(max_length=32, blank=True)
    number_of_users = models.IntegerField(default=0, validators=[MaxValueValidator(800000000), MinValueValidator(0)])

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
        # db_table = "Rooms"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('room_detail', args=[str(self.id)])
