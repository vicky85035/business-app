from django.shortcuts import render
from rest_framework import generics
from business.models import Business, Branch
from business.serializers import BusinessSerializer, BranchSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
class BusinessListCreate(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BranchListCreate(generics.ListCreateAPIView):
    serializer_class = BranchSerializer

    # def get_queryset(self):
    #     queryset = Branch.objects.all()

    #     business_id = self.request.query_params.get('business_id',None)

    #     if business_id:
    #         queryset = queryset.filter(business__id=business_id)
    #     return queryset
    
    
    def get_queryset(self):
        business = get_object_or_404(Business, id=self.kwargs['business_id'])
        return Branch.objects.filter(business__id=business.id).order_by('created_at')