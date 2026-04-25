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



class AccountType(BaseClass):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = "main_account_type"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"


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

class RecruitmentCategory(BaseClass):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = "main_recruitment_category"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"


class Recruitment(BaseClass):
    uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.OneToOneField(RecruitmentCategory, on_delete= models.SET_NULL, null=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)

    class Meta:
        db_table = "main_recruitments"

    def __str__(self):
        return f" {self.category} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en} {self.file}"


class SchemeCategory(BaseClass):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = "main_scheme_category"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"

class Scheme(BaseClass):
    uuid = models.UUIDField(max_length=64, default=uuid.uuid4, editable=False)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.ForeignKey(SchemeCategory, on_delete= models.SET_NULL, null=True)
    file = models.FileField(upload_to="files/", null=True, blank=True)
    slug = models.SlugField(unique=True, null=True, blank=True)

    class Meta:
        db_table = "main_schemes"

    def __str__(self):
        return f" {self.category} {self.name_hi} {self.name_en} {self.description_hi} {self.description_en} {self.file}"


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

class UtilityCategory(BaseClass):
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    class Meta:
        db_table = "main_utility_category"

    def __str__(self):
        return f"{self.name_hi} {self.name_en}"

class Utility(BaseClass):
    uuid = models.CharField(max_length=64, default=uuid.uuid4, editable=False)
    #app_code = models.CharField(max_length=100, unique=True)
    #app_url = models.URLField(max_length=556)
    name_hi = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_hi = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="images/", blank=True, null=True)
    category = models.OneToOneField(UtilityCategory, on_delete= models.SET_NULL, null=True)
    #file = models.FileField(upload_to="files/", null=True, blank=True)

    class Meta:
        db_table = "main_utilities"

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

class Venue(BaseClass):

        TAG_CHOICES = [
            ('Samarth', 'Samarth/समर्थ'),
            ('Saksham', 'Saksham/सक्षम'),
            ('Samridhh', 'Samridhh/समृद्ध')
        ]

        STATUS_CHOICES = [
           ('Active' , 'Active'),
            ('Inactive' , 'Inactive')   
        ]

        tehsil = models.ForeignKey(Tehsil, on_delete=models.CASCADE, null=True, blank=True)
        uuid=models.UUIDField(unique=False, null=False, blank=True, default=uuid.uuid4)
        url=models.URLField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        time=models.TimeField(unique=False, null=False, blank=True, default = timezone.now)
        #small_auto=models.SmallAutoField( unique=False, null=False, blank=True, default=   ' ')
        slug=models.SlugField(max_length=255, unique=True, null=False, blank=True, default=   ' ')
        postitive_small_integer=models.PositiveSmallIntegerField( unique=False, null=True, blank=True, default=   ' ')
        postitive_integer=models.PositiveIntegerField( unique=False, null=True, blank=True, default=   ' ')
        postitive_big_integer=models.PositiveBigIntegerField( unique=False, null=True, blank=True, default=   ' ')
        many_to_many=models.ManyToManyField('SchemeCategory', blank=True)
        generic_ipaddress=models.GenericIPAddressField( unique=False, null=True, blank=True, default=   ' ')
        #ipaddress=models.IPAddressField( unique=False, null=False, blank=True, default=   ' ')
        integer=models.IntegerField(unique=False, null=False, blank=True, default=0)
        photo=models.ImageField(unique=False, null=False, blank=True, default=   ' ')
        destination_price=models.FloatField(unique=False, null=False, blank=True, default=   ' ')
        email=models.EmailField(max_length=255, unique=True, null=False, blank=True, default=   ' ')
        duration=models.DurationField( unique=False, null=True, blank=True)
        created_at=models.DateTimeField( unique=False, null=True, blank=True, default = timezone.now)
        updated_at=models.DateTimeField( unique=False, null=True, blank=True, default = timezone.now)
        status=models.BooleanField( unique=False, null=False, blank=True)
        date=models.DateField( unique=False, null=True, blank=True, default = timezone.now)
        hash=models.BinaryField( unique=False, null=False, blank=True)
        name_hi=models.CharField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        name_en=models.CharField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        address_hi=models.CharField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        address_en=models.TextField( unique=False, null=False, blank=True, default=   ' ')
        contact=models.CharField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        areas_available=models.CharField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        menus=models.FileField(unique=False, null=False, blank=True, default=   ' ')
        gallery=models.JSONField(unique=False, null=False, blank=True, default=dict)
        description_hi=models.TextField( unique=False, null=False, blank=True, default=   ' ')
        description_en=models.TextField( unique=False, null=False, blank=True, default=   ' ')
        rooms=models.IntegerField( unique=False, null=False, blank=True, default=0)
        hotel_area=models.CharField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        garden_area=models.CharField(max_length=255, unique=False, null=False, blank=True, default=   ' ')
        parking=models.BooleanField( unique=False, null=False, blank=True, default=   ' ')
        room_price=models.IntegerField( unique=False, null=True, blank=True, default=   ' ')
        garden_rate=models.IntegerField( unique=False, null=True, blank=True, default=   ' ')
        verify_status=models.CharField(max_length=255, unique=False, null=False, blank=True, choices= STATUS_CHOICES, default='Active')
        #id=models.AutoField( unique=False, null=False, blank=True, default=   ' ')
        #record=models.BigAutoField( unique=False, null=False, blank=True, default=   ' ')
        mobile=models.BigIntegerField( unique=True, null=False, blank=True, default=   ' ')
        documents=models.FilePathField(unique=False, null=False, blank=True, path = "/srijan/images")
        tags =models.CharField(max_length=255, unique=False, null=False, blank=True, choices= TAG_CHOICES, default='General')

        class Meta:
            db_table = "main_venues"

        def __str__(self):
            return f" {self.name_hi} {self.name_en} "

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


class LssemsService(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name}"

class ServiceProvider(models.Model):
    
    STATUS_CHOICES = [
        ("New", "New"),
        ("Active" , "Active"),
        ("Inactive", "Inactive"),
        ("Disabled", "Disabled"),
        ("Deleted", "Deleted"),
        ("Marked", "Marked")
    ]

    unique_id = models.UUIDField(default=uuid.uuid4, editable = False) 
    details = models.TextField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='uploads/', max_length=100)
    service = models.ForeignKey(LssemsService, models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now(), blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    status = models.CharField(default="New", choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.name}"
