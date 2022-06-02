from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

import threading

from .models import SpecialUser
from .token import generate_token


# registration confirmation   https://github.com/CryceTruly/django-tutorial-youtube/blob/main/authentication/views.py

class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send()


def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Activate your account'
    email_body = render_to_string('registration/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generate_token.make_token(user)
    })

    email = EmailMessage(subject=email_subject, body=email_body,
                         from_email=settings.EMAIL_FROM_USER, to=[user.email]
                         )

    if not settings.TESTING:
        EmailThread(email).start()


# @auth_user_should_not_access
def register(request):
    if request.method == 'POST':
        context = {'has_error': False, 'data': request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(password1) < 6:
            messages.add_message(request, messages.ERROR, 'Password must be at least 6 characters')
            context['has_error'] = True

        if password1 != password2:
            messages.add_message(request, messages.ERROR, 'Passwords does not match')
            context['has_error'] = True

        # needs to be fixed with email validator (Nizami's Responsibility)

        # if not validate_email(email):
        #     messages.add_message(request, messages.ERROR, 'Enter a valid email address')
        #     context['has_error'] = True

        if not username:
            messages.add_message(request, messages.ERROR, 'Username is required')
            context['has_error'] = True

        if SpecialUser.objects.filter(username=username).exists():
            messages.add_message(request, messages.ERROR, 'This username already exist')
            context['has_error'] = True

            return render(request, 'registration/signup.html', context, status=409)

        if context['has_error']:
            return render(request, 'registration/signup.html', context)

        user = SpecialUser.objects.create_user(username=username, email=email)
        user.set_password(password1)
        user.save()

        if not context['has_error']:
            send_activation_email(user, request)

            messages.add_message(request, messages.SUCCESS, "We sent you an email to verify your account")

            return redirect('success')

    return render(request, 'registration/signup.html')


# @auth_user_should_not_access
def login_user(request):
    if request.method == 'POST':
        context = {'data': request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(request, username=username, password=password)

        if user and not user.is_email_verified:
            messages.add_message(request, messages.ERROR, 'Email is not verified, please check your email inbox')
            return render(request, 'registration/login.html', context, status=401)

        if not user:
            messages.add_message(request, messages.ERROR, 'Account with this username does not exist, try again')
            return render(request, 'registration/login.html', context, status=401)

        login(request, user)

        messages.add_message(request, messages.SUCCESS, f'Welcome {user.username}')
        return redirect(reverse('main'))

    return render(request, 'registration/login.html')


def logout_user(request):
    logout(request)

    messages.add_message(request, messages.SUCCESS, 'Successfully logged out')

    return redirect(reverse('login'))


def activate_user(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = SpecialUser.objects.get(pk=uid)

    except Exception as e:
        user = None

    if user and generate_token.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(request, messages.SUCCESS, "Email Verified, now you can log in")
        return redirect(reverse('login'))

    return render(request, 'registration/activate-failed.html', {"user": user})


def signup_success(request):
    return render(request, 'registration/signup_success.html')
