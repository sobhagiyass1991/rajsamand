from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 100)
    status = models.BooleanField(default=True)
    #randomid = models.BigIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)