import uuid
from django.utils import timezone
from django.db import models
from main.models import Tehsil

class Venue(models.Model):

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
        #many_to_many=models.ManyToManyField('SchemeCategory', blank=True)
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
            db_table = "events_venues"

        def __str__(self):
            return f" {self.name_hi} {self.name_en} "

class EventList(models.Model):
    title = models.CharField(max_length = 100)
    status = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    