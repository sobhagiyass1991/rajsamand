from django.db import models
import uuid 

class SchemeCategory(models.Model):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField()

    class Meta:
        db_table = "government_scheme_category"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"

class Scheme(models.Model):
    uuid = models.UUIDField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(SchemeCategory, on_delete= models.SET_NULL, null=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField()
    
    class Meta:
        db_table = "government_schemes"

    def __str__(self):
        return f" {self.category} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en} {self.file}"
