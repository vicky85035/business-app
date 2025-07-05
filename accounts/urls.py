from django.urls import path
from accounts.views import UserListAPI

urlpatterns = [
    path('user_list/', UserListAPI.as_view(), name='user-list-api')
]