import os 
import random 
import uuid
from django.db import models
from django.contrib.auth.models import User, AbstractUser
import random
from django.utils import timezone
from django.conf import settings 
from django.core.validators import FileExtensionValidator

class BaseClass(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    phone = models.CharField(max_length=15)
    message = models.TextField(null=True, blank=True)
    document = models.FileField(
        upload_to='images',
        validators= [FileExtensionValidator(['pdf', 'doc', 'docx', 'txt'])],
        blank = True,
        null = True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contacts'
    )
    
    class Meta:
        db_table = "main_contacts"
        unique_together = ('name', 'email')

    def __str__(self):
        return f"{self.name} {self.email} {self.phone} {self.message}"

class Message(BaseClass):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=False)
    mobile = models.CharField(max_length=15)
    message = models.TextField(null=True, blank=True)
    
    class Meta:
        db_table = "main_messages"

    def __str__(self):
        return f"{self.name} {self.email} {self.mobile} {self.message}"

class NotificationCategory(BaseClass):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = "main_notification_category"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"


class Notification(BaseClass):
    uuid = models.UUIDField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.OneToOneField(NotificationCategory, on_delete= models.SET_NULL, null=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)

    class Meta:
        db_table = "main_notifications"

    def __str__(self):
        return f" {self.category} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en} {self.file}"

class PageVisit(BaseClass):
    page_url = models.URLField(max_length=556)
    visit_count = models.BigIntegerField(default=0, unique=True)
    last_visited = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "main_page_visit"

    def __str__(self):
        return f" {self.page_url} {self.visit_count} {self.last_visited}"


class SystemSetting(BaseClass):
#    uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    contact = models.IntegerField(unique=True,null=True, blank=True)
    logo = models.ImageField(upload_to="images/", blank=True, null=True)
#   address = ...

    class Meta:
        db_table = "main_system_settings"

    def __str__(self):
        return f" {self.name_hi} {self.name_en}  {self.email} {self.contact} {self.logo}"


    
class Tehsil(BaseClass):
#    uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = "main_tehsils"

    def __str__(self):
        return f" {self.name_hi}  {self.name_en} {self.image}"

class TouristPlace(BaseClass):
    #uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    #category = models.OneToOneField(NotificationCategory, on_delete= models.SET_NULL, null=True)
    #file = models.FileField(upload_to="files/", null=True, blank=True)

    class Meta:
        db_table = "main_tourist_places"

    def __str__(self):
        return f" {self.category} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en} {self.file}"


class UserAppCategory(BaseClass):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = "main_userapp_category"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"

class UserApp(BaseClass):
    uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    app_code = models.CharField(max_length=100, unique=True)
    app_url = models.URLField(max_length=556)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.OneToOneField(UserAppCategory, on_delete= models.SET_NULL, null=True)
    #file = models.FileField(upload_to="files/", null=True, blank=True)

    class Meta:
        db_table = "main_userapp"

    def __str__(self):
        return f" {self.category} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en}"

class Webpage(BaseClass):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = "main_webpages"

    def __str__(self):
        return f" {self.slug} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en}"

class Location(BaseClass):
    district_hi = models.CharField(max_length=255)
    district_en = models.CharField(max_length=255)
    tehsil_hi = models.CharField(max_length=255)
    tehsil_en = models.CharField(max_length=255)
    gram_panchayat_hi = models.TextField(null=True, blank=True)
    gram_panchayat_en = models.TextField(null=True, blank=True)
    village_hi = models.TextField(null=True, blank=True)
    village_en = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "main_locations"

    def __str__(self):
        return f" {self.district_hi} {self.tehsil_en} {self.gram_panchayat_en} {self.village_en}"

def docs_path(self):
      return os.path.join(settings.LOCAL_FILE_DIR, "images")


class Pincode(BaseClass):
    state =models.CharField(max_length=255, unique=False, null=False, blank=True, default='Rajasthan')
    district =models.CharField(max_length=255, unique=False, null=False, blank=True, default='Rajsamand')
    office =models.CharField(max_length=255, unique=False, null=False, blank=True, default='')
    circle =models.CharField(max_length=255, unique=False, null=False, blank=True, default='')
    pincode = models.CharField(max_length=6, blank=False)
    
    class Meta:
        db_table = "main_pincodes"

    def __str__(self):
        return f"{self.pincode}"


