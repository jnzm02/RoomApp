# Generated by Django 4.0.1 on 2022-07-18 06:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0011_alter_room_room_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_members',
            field=models.ManyToManyField(related_name='room_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(max_length=32, unique=True),
        ),
    ]