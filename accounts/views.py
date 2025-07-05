from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import UserSerializer
from accounts.models import User

class UserListAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()