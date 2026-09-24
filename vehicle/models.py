from django.db import models
class VehicleList(models.Model):
    title = models.CharField(max_length = 100)
    status = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    

# Create your models here.
