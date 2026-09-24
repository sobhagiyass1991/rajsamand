from django.contrib.auth.models import User
from django.db import models
import uuid
from ckeditor.fields import RichTextField
from main.models import Tehsil
#from django.config import settings
from django.conf import settings 

class JobList(models.Model):
    title = models.CharField(max_length = 100)
    status = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Jobslist(models.Model):
    TYPES = [
        ('Onsite','Onsite'),
        ('Remote','Remote'),
        ('Hybrid', 'Hybrid'),
    ]

    postname = models.CharField(max_length=100)
    jobtype = models.CharField(choices=TYPES, default='Onsite', max_length=50, null=True, blank=True)
    posts = models.PositiveIntegerField(null=True, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(max_length=512, null=True, blank=True)
    description = RichTextField()
    #tehsil = models.ForeignKey(Tehsil, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="jobcreatedby")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"{self.postname}"
    

class RecruitmentCategory(models.Model):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        db_table = "jobs_recruitment_category"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"


class Recruitment(models.Model):
    uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.OneToOneField(RecruitmentCategory, on_delete= models.SET_NULL, null=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        db_table = "jobs_recruitments"

    def __str__(self):
        return f" {self.category} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en} {self.file}"
