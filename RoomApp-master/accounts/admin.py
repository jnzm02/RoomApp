from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import SpecialUser


# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    change_form = CustomUserChangeForm
    model = SpecialUser


admin.site.register(SpecialUser, CustomUserAdmin)
