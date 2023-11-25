from django.db import models
from userapp.models import *
# Create your models here.

class info_bulk_keyword_model(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    keyword_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')
    error = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name