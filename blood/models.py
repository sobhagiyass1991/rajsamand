from django.db import models
from django.conf import settings 

# Create your models here.
class Donor(models.Model):
    BLOOD_GROUP = {
        "A+": "A+",
        "A-": "A-",
        "B+": "B+",
        "B-": "B-",
        "AB+": "AB+",
        "AB-": "AB-",
        "O+": "O+",
        "O-": "O-"
    }
    name  = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    email = models.EmailField()
    #blood_group = models.CharField(max_length=5, choices = BLOOD_GROUP) 
    blood_group = models.CharField(max_length=5, choices = BLOOD_GROUP) 
    status = models.BooleanField(default=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Donation(models.Model):
    donorname = models.ForeignKey(Donor, on_delete=models.CASCADE)
    blood_group = models.CharField(null=True, blank=True) 
    status = models.BooleanField(default=True)
    volume = models.FloatField(null=True, blank=True)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Requestt(models.Model):
    BLOOD_GROUP = {
        "A+": "A+",
        "A-": "A-",
        "B+": "B+",
        "B-": "B-",
        "AB+": "AB+",
        "AB-": "AB-",
        "O+": "O+",
        "O-": "O-"
    }
    patientname = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5, choices = BLOOD_GROUP) 
    status = models.BooleanField(default=True)
    volume = models.FloatField(null=True, blank=True)
    doctorname = models.CharField(max_length=100)
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, **kwargs):
        self.volume = self.volume + 10
        print(f"volume is {self.volume}")
        super().save(**kwargs)