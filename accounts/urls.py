from shapes_app import views
from .views import api_register, api_user_details, api_login
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('api/user/', api_user_details, name='api_user'),
    path('api/register/', api_register, name='api_register'),
    path('api/login/', api_login, name='api_login'),
]