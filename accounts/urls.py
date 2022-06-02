from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.register, name='signup'),
    path('login/', views.login_user, name='login'),
    path('success/', views.signup_success, name='success'),
    path('logout/', views.logout_user, name='logout'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('resend-verification/', views.resend_email, name='resend'),
]
