from django.contrib import admin
from business.models import Category,Marketing,Business,Branch,Address,WebPortal

# Register your models here.
admin.site.register([Category,Marketing,Business,Branch,Address,WebPortal])