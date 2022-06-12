from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files import File


# see the video on https://www.youtube.com/watch?v=xSUm6iMtREA
# class ImageForUser(models.Model):

class SpecialUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    # need to explore models to connect the user with rooms available for him/her
    # rooms_available

    # in the future it is expected that we will have profiles for users (with username, email, bios, and photos)
    # so it is expected that we will update model 'SpecialUser'

    # TODO: bio = models.CharField(max_length=1000)
    bio = models.TextField(default="", max_length=1000)

    # TODO: photo = models.ImageField(default='images/blank-profile-picture')
    # profile_image = models.ImageField(upload_to='profile_images', default='images/blank-profile-picture')
    # upload_should to be integrated to media folder 'profile images'
    # see the video 'https://www.youtube.com/watch?v=xSUm6iMtREA'
