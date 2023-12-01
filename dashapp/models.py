from django.db import models
from userapp.models import *

# Create your models here.

class Logo(models.Model):
    logo_img = models.ImageField(upload_to='images/')
    icon_img = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return 'Logo'
        


class ApiList(models.Model):
    api_name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=300)
    filled_quota = models.PositiveIntegerField(default=0)
    website_quota_limit = models.PositiveIntegerField()
    error_status = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.api_name} : Working for - ( {self.filled_quota} operation ) of ( {self.website_quota_limit}  Quota  ) , API key : {self.api_key}"


class Website_List(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    website_name = models.CharField(max_length=250)
    website_url = models.URLField()
    username = models.CharField(max_length=250, null=True, blank=True)
    application_password = models.CharField(max_length=250)

    def __str__(self):
        return f"Website Name : {self.website_name}"


class Youtube_api(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=150)
    API_Key = models.CharField(max_length=500)
    error_status = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.name