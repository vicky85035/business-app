from django.urls import path
from business.views import BusinessListCreate 

urlpatterns = [
    path('business_list/', BusinessListCreate.as_view(), name = 'business-list-create')
]