from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files import File
# Create your models here.

#class ImageForUser(models.Model):

class SpecialUser(AbstractUser):
    pass
    # username = models.CharField(max_length=150)
    # email = models.EmailField(max_length=100)

