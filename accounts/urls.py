from shapes_app import views
from .views import api_register, api_user_details, api_login, user_view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('user/', user_view.as_view(), name='api_user'),
    path('register/', user_view.as_view(), name='api_register'),
    path('login/', user_view.as_view(), name='api_login'),
]