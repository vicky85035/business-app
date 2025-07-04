from django.shortcuts import render
from rest_framework import generics
from business.models import Branch
from business.serializers import BusinessSerializer
from rest_framework.response import Response

# Create your views here.
class BusinessListCreate(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BusinessSerializer

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        new_list = []
        count = 0
        for branches in response.data:
            # breakpoint()
            count += 2
            new_list.append({
                'id': branches['id'],
                'Business': branches['business'],
                'Created_at': branches['created_at'],
                'Category': branches['category'],
                'No. of locations': count
            })
        result = Response(new_list)
        return result