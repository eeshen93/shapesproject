from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('shapes/', views.shapes_view.as_view(), name="api-shapes"),
    path('create-shape/', views.shapes_view.as_view(), name="api-create"),
    path('update-shape/<str:pk>/', views.shapes_view.as_view(), name="api-update"),
    path('delete-shape/<str:pk>/', views.shapes_view.as_view(), name="api-delete"),
    
]