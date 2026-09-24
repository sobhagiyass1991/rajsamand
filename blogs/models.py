from django.db import models
from django.conf import settings 
#from tinymce.models import HTMLField

class BlogList(models.Model):
    title = models.CharField(max_length = 100, null=True, blank=True)
    text = models.CharField(null=True, blank=True)
    image = models.ImageField(upload_to="upload/", null=True, blank=True)
    status = models.BooleanField(default=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    