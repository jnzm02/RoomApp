# Generated by Django 4.0.1 on 2022-06-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_specialuser_is_email_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialuser',
            name='bio',
            field=models.TextField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='specialuser',
            name='profile_image',
            field=models.ImageField(default='blank-profile-picture.png', upload_to='profile_images'),
        ),
    ]