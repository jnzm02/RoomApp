# Generated by Django 4.0.1 on 2022-06-21 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0007_room_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_image',
            field=models.ImageField(default='images/icon.jpg', upload_to='room_images'),
        ),
    ]
