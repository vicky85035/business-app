from django.shortcuts import render
from rest_framework import generics
from accounts.serializers import UserSerializer
from accounts.models import User
from django.db.models import Count

class UserListAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return super().get_queryset().annotate(user_count=Count('branches'))