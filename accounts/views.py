from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import login, get_user_model, authenticate
from django.views.generic import CreateView, TemplateView
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage, send_mail

from .models import SpecialUser
from .forms import CustomUserCreationForm, UserChangeForm, SignupForm
from .token import account_activation_token
# Create your views here.

# before registration confirmation
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('main')


# registration confirmation view
# https://www.javatpoint.com/django-user-registration-with-email-confirmation
# def signup(request):
#     User = get_user_model()
#     if request.method == 'POST':
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             #save form in the memory not in database
#             email = form.cleaned_data('email')
#             if SpecialUser.objects.filter(email__iexact=email).count() == 1:
#                 user = form.save(commit=False)
#                 user.is_active = False
#                 user.save()
#                 #to get the domain of the current site
#                 current_site = get_current_site(request)
#                 mail_subject = 'Activation link has been sent to your email id'
#                 message = render_to_string('email_activation.html', {
#                     'user':user,
#                     'domain': current_site.domain,
#                     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
#                     'token': account_activation_token.make_token(user),
#                     })
#                 to_email = form.cleaned_data.get('email')
#                 send_mail(mail_subject, message, 'youremail', [to_email])
#                 return HttpResponse('Please confirm your email address to complete the registration')
#     else :
#         form = SignupForm()
#     return render(request, 'registration/signup.html', {'form':form})

# def activate(request, uidb64, token):
#     User = get_user_model()
#     try:
#         uid = force_str(urlsafe_base64_decode(uidb64))
#         user = User.object.get(pk=uid)
#     except(TypeError, ValueError,  OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and account_activation_token.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return HttpResponse("Thank you for your email confirmation. Now you can login your account.")
#     else:
#         return HttpResponse("Activation link is invalid!")
