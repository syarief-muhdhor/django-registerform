from django.urls import path
from .views import *

urlpatterns = [
    path('', RegisterFormView.as_view(), name='dashboard'),
    path('visitor/register/', RegisterFormView.as_view(), name='visitor-register'),
    path('visitor/login/', LoginView.as_view(), name='visitor-login')
]
