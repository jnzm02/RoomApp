# Generated by Django 4.0.1 on 2022-06-10 19:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_remove_room_entered_password_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='online_users',
        ),
    ]
