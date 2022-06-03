from django.contrib import admin
from django.urls import path, include
from . import views
from accounts import views as accountviews
urlpatterns = [
    path('', views.main, name='home'),
    path('login', views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register', views.registerpage, name='register'),
    path('shapes', views.shapes, name='shapes'),
]
