from django.db import models
from django.conf import settings 

class PropertyList(models.Model):
    bedrooms=models.PositiveSmallIntegerField(null=True,blank=True)
    bathrooms=models.PositiveSmallIntegerField(null=True,blank=True)
    balconies=models.PositiveSmallIntegerField(null=True,blank=True)
    furnishing_status=models.CharField(max_length = 100,null=True,blank=True)
    title = models.CharField(max_length = 100, null=True, blank=True)
    ptype = models.CharField(null=True, blank=True)
    area = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='uploads/', null=True, blank=True)
    features = models.JSONField(null=True, blank = True)
    configs = models.CharField(null=True, blank=True)
    bedrooms=models.PositiveSmallIntegerField(max_length = 100,null=True,blank=True)
    status = models.BooleanField(default=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    print(f" the type of title is {type(title)}")
    print(f" the type of title is {vars(bedrooms)}")