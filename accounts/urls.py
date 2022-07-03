from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [

    # Registration
    path('signup/', views.register, name='signup'),
    path('success/', views.signup_success, name='success'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
    path('resend-verification/', views.resend_email, name='resend'),

    # Log In and Log Out
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    # SpecialUser Profile
    path('profile/<str:username>/', login_required(views.get_user_profile), name='user_profile'),
    # path('profile/<str:username>/edit', views.edit_profile, name='edit_profile')
]
