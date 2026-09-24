from django.db import models
from django.conf import settings 
from django_ckeditor_5.fields import CKEditor5Field
from tinymce_4.fields import TinyMCEModelField

class Category(models.Model):
    title = models.CharField(max_length = 100)
    status = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class ItemList(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    ownername = models.CharField(max_length=100, null=True, blank=True)
    description = TinyMCEModelField('Foo content')
    image = models.ImageField(upload_to="upload/", null=True, blank=True)
    title = models.CharField(max_length = 100)
    status = models.BooleanField()
    created_by  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    