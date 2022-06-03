from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('shapes/', views.api_shapes, name="api-shapes"),
    path('create-shape/', views.api_create_shape, name="api-create"),
    path('update-shape/<str:pk>/', views.api_update_shape, name="api-update"),
    path('delete-shape/<str:pk>/', views.api_delete_shape, name="api-delete"),
    
]