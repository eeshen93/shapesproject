from django.shortcuts import render
from requests import post
from .forms import CreateUserForm
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from api.views import api_shapes
import json


# Create your views here.
def main(request):
    
    return render(request,'main.html')


def loginpage(request):
  
    
    if request.method == "POST":
      email = request.POST.get('email')
      password = request.POST.get('password')
      user = authenticate(request, email=email, password=password)

      if user is not None:
        login(request, user)
        
      else:
        
        messages.error(request,'Email / password is incorrect or email is unverified.')

    
    return render(request, 'login1.html')


def registerpage(request):
    return render(request,'register.html')


def logoutuser(request):
    if request.user.is_authenticated:
        logout(request)
    return HttpResponseRedirect('/login')

def shapes(request):
    if request.user.is_authenticated:
        return render(request,'shapes.html')
    else:
        messages.error(request,'Please login to use Shapes.')
        return render(request, 'login1.html')