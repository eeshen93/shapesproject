from urllib import response
from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
#from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.decorators import api_view
from .models import customuser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
# Create your views here.


@api_view(['GET'])
def api_user_details(request):
    user=customuser.objects.get(id=request.user.id)
    serializer=UserSerializer(user)
    return Response(serializer.data)


@api_view(['POST'])
def api_register(request):

    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        password2=request.POST.get('password2')
    data1={
        'username':username,
        'email':email,
        'password':password,
        'password2':password2}
    
    serializer=RegisterSerializer(data=data1)
    data={}
    if serializer.is_valid():
        user = serializer.save()
        data['response']="New user created!"
        data['email']=user.email
        data['username']=user.username
        token=Token.objects.get(user=user.id).key
        data['token']=token
        
    else:
        data=serializer.errors
    return Response(data)

@api_view(['POST'])
def api_login(request):

    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
    
        data={}  
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            token=Token.objects.get(user=user).key
            data['email']=email
            data['username']=user.username
            data['token']=token
            
        else:
            data['error']='Login error, try again.'
        return Response(data)



