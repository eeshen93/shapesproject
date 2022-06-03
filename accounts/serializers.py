from rest_framework import serializers
from .models import customuser
#from django.contrib.auth.models import User

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = customuser
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model = customuser
        fields = ('id', 'username', 'email', 'password', 'password2')
        extra_kwargs = {'password': {'write_only': True}}

    def save(self):
        user = customuser(email=self.validated_data['email'], username=self.validated_data['username'])
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        ## make sure passwords are matching ##

        if password != password2:
            raise serializers.ValidationError({'password': 'Error, passwords must match.'})

        user.set_password(password)
        user.save()
        return user

