from django.shortcuts import render
from rest_framework import generics
from business.models import Branch, Business
from business.serializers import BusinessSerializer
from rest_framework.response import Response

# Create your views here.
class BusinessListCreate(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return Response(response.data)