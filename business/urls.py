from django.urls import path
from business.views import BusinessListCreate, BranchListCreate

urlpatterns = [
    path('business_list/', BusinessListCreate.as_view(), name = 'business-list-create'),
    path('<int:business_id>/branch_list/', BranchListCreate.as_view(), name = 'branch-list-create'),
]