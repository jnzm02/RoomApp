from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import SpecialUser


class SpecialUserUpdateProfileForm(ModelForm):
    class Meta:
        model = SpecialUser
        fields = ['bio', 'profile_image']

# this form created before 'registration verification done
# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm):
#         model = SpecialUser
#         fields = ('username', 'email')
#
#     help_texts = {
#         'username': None
#     }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['password1'].help_text = None
#         self.fields['password2'].help_text = None


# this form created before 'registration verification done
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = SpecialUser
        fields = UserChangeForm.Meta.fields


# class EditProfileForm(UserChangeForm):
#
#     class Meta:
#         model = SpecialUser
#         fields = ('username', 'email')
#
#
# class UpdateProfileForm(forms.ModelForm):
#
#     class Meta:
#         model = SpecialUser
#         fields = ('bio', 'profile_image')


# this is new form for email verification
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text="Required")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
