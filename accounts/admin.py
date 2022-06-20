from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SignupForm, CustomUserChangeForm
from .models import SpecialUser


class CustomUserAdmin(UserAdmin):
    # add_form = CustomUserCreationForm
    add_form = SignupForm
    change_form = CustomUserChangeForm
    model = SpecialUser


admin.site.register(SpecialUser, CustomUserAdmin)
