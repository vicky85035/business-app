from django.contrib import admin
from accounts.models import UserManager,User,ContactList,AgencyStaff

# Register your models here.
admin.site.register([User,ContactList,AgencyStaff])