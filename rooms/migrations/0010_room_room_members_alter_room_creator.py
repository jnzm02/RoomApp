# Generated by Django 4.0.1 on 2022-06-22 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rooms', '0009_room_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_members',
            field=models.ManyToManyField(related_name='room_member', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='creator',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]
