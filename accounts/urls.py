from django.urls import path
from accounts import views
from .views import SignUpView

urlpatterns = [ 
    path('signup/', SignUpView.as_view(), name='signup'),
]