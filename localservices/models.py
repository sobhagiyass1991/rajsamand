from django.db import models
from django.utils import timezone
from django.conf import settings 
import uuid

# Create your models here.
class LssemsService(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class ServiceProvider(models.Model):
    
    STATUS_CHOICES = [
        ("New", "New"),
        ("Active" , "Active"),
        ("Inactive", "Inactive"),
        ("Disabled", "Disabled"),
        ("Deleted", "Deleted"),
        ("Marked", "Marked")
    ]

    unique_id = models.UUIDField(default=uuid.uuid4, editable = False) 
    details = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', max_length=100)
    service = models.ForeignKey(LssemsService, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(default="New", choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name}"
