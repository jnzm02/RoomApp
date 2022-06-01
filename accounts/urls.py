from django.urls import path
from accounts import views
from .views import SignUpView

urlpatterns = [
    # path('singup/', views.sinupuser, name='signupuser'),  
    path('signup/', SignUpView.as_view(), name='signup'),
]