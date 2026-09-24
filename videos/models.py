from django.db import models
from django.conf import settings 

class VideoList(models.Model):
    title = models.CharField(null=True, blank=True)
    video_file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)
    status = models.BooleanField(default=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"        
# Create your models here.
