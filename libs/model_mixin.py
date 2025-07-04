from django.db import models

class BaseModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True
        # ordering = ['-created_at'] # Order by creation date, newest first
