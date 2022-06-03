from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from accounts.models import customuser

# Create your models here.

class Shape(models.Model):
    user = models.ForeignKey(customuser, on_delete = models.SET_NULL, default=1,null=True, blank=True)
    shape_type=models.CharField(max_length=50, blank=True, null=True)
    side1=models.FloatField(blank=True, null=True)
    side2=models.FloatField(blank=True, null=True)
    side3=models.FloatField(blank=True, null=True)
    area=models.FloatField(blank=True, null=True)
    perimeter=models.FloatField(blank=True, null=True)
    msg=models.CharField(max_length=100, blank=True, null=True)
    
    
