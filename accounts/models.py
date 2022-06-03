# Create your models here.
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User, AbstractUser, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# Create your models here.

class customuser(AbstractUser):
    email=models.EmailField(unique=True)
    username=models.CharField(max_length=50, unique=True)
    
    REQUIRED_FIELDS= ['username']
    USERNAME_FIELD= 'email'

    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)