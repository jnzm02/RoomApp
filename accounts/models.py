from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.files import File


class SpecialUser(AbstractUser):
    is_email_verified = models.BooleanField(default=False)

    # TODO: check if some user is_online or not
    # see the link https://stackoverflow.com/questions/29663777/how-to-check-whether-a-user-is-online-in-django-template
    # in the future it is expected that we will have profiles for users (with username, email, bios, and photos)
    # so it is expected that we will update model 'SpecialUser'

    # TODO: bio = models.CharField(max_length=1000)
    bio = models.TextField(blank=True, max_length=1000)

    # FIXME: cannot assign default value as blank.jpg
    profile_image = models.ImageField(upload_to='profile_images',
                                      default='images/blank.jpg', blank=False, null=False)
    rooms = models.ManyToManyField('rooms.Room', blank=True)
    number_of_rooms = models.IntegerField(default=0)
    # upload_should to be integrated to media folder 'profile images'
    # see the video 'https://www.youtube.com/watch?v=xSUm6iMtREA'

    def __str__(self):
        return self.username
