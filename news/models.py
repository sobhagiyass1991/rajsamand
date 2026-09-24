from django.db import models
from django.conf import settings 

class Category(models.Model):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_en}"

class NewsList(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length = 100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.category} {self.title}"
            