# Generated by Django 4.0.1 on 2022-06-14 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_remove_room_online_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_private',
            field=models.BooleanField(default=False),
        ),
    ]
