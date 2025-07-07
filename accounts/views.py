from django.shortcuts import render
from rest_framework import generics, filters
from accounts.serializers import UserSerializer
from accounts.models import User
from django.db.models import Count
from business.pagination import SetPagination

class UserListAPI(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['email', 'no_of_locations']
    ordering = ['date_joined']
    pagination_class = SetPagination

    def get_queryset(self):
        return super().get_queryset().annotate(user_count=Count('branches'))