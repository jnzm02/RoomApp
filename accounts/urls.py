from django.urls import path
from . import views
from .views import register, logout_user, login_user, activate_user

urlpatterns = [
    # path('signup/', SignUpView.as_view(), name='signup'),
    path('signup/', views.register, name='signup'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('activate-user/<uidb64>/<token>', views.activate_user, name='activate'),
]
