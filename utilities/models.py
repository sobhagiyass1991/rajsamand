import uuid
from django.db import models
from main.models import Tehsil

class UtilityCategory(models.Model):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Utility(models.Model):
    uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    #app_code = models.CharField(max_length=100, unique=True)
    #app_url = models.URLField(max_length=556)
    name_hi = models.CharField(max_length=255, null=True, blank=True)
    name_en = models.CharField(max_length=255, null=True, blank=True)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    address = models.TextField(max_length=512, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True, help_text="State name in English", default="Rajasthan")
    district = models.CharField(max_length=35, null=True, blank=True, default="Rajsamand")
    division = models.CharField(null=True, blank=True)
    subdivision = models.ForeignKey(Tehsil, on_delete=models.SET_NULL, null=True, blank=True)
    phone  = models.CharField(max_length=15, null=True, blank=True) 
    mobile  = models.CharField(max_length=15, null=True, blank=True)
    designation = models.CharField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True) 
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(UtilityCategory, on_delete= models.SET_NULL, null=True)
    extrainfo = models.JSONField(null=True, blank=True)
    #file = models.FileField(upload_to="files/", null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    #def __str__(self):
    #    return f"{self.category}"    

# Create your models here.
