import uuid
import random 
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Role(models.Model):
      name = models.CharField(max_length=100, unique=True)
      def __str__(self):
            return f"{self.name}"

class User(AbstractUser):
    'null=True'

    ACCOUNT_TYPES = [
        ('Individual', 'Individual'),
        ('Business', 'Business'),
        ('Organization', 'Organization')
    ]

    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Transgender', 'Transgender')
    ]

    STATUS = [
        ('New', 'New'),
        ('Active','Active'),
        ('Inactive','Inactive'),
        ('Banned','Banned'),
        ('Deleted', 'Deleted')

    ]

    srijan_id = models.BigIntegerField(null=True, blank=True)
    srijan_key = models.CharField(max_length=64, default=uuid.uuid4, editable=False, blank=True)
    #first_name = models.CharField(max_length=255, null=True, blank=True)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    #last_name = models.CharField(max_length=255 , null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    #username = models.CharField(max_length=255, unique=True, null=True, blank=True)
    mobile = models.CharField(max_length=15, null=True, blank=True)
    gender = models.CharField(default='Male', choices=GENDER, max_length=30, null=True, blank=True)
    address = models.TextField(max_length=512, null=True, blank=True)
    locale = models.CharField(max_length=10, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    account_type = models.CharField(choices=ACCOUNT_TYPES, default='Individual', max_length=50, null=True, blank=True)
    #last_login = models.DateTimeField(auto_now=True, null=True, blank=True)
    profile_pic = models.ImageField(upload_to="profiles/", blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS, default='New', null=True, blank=True)
    role = models.ForeignKey(Role, on_delete=models.SET_NULL, null = True, blank = True)
    
    class Meta:
       db_table = "accounts_users"

    def save(self, *args, **kwargs):
        if not self.srijan_id:
            # एक यूनिक 10 अंकों की ID जेनरेट करना (आप अपने हिसाब से बदल सकते हैं)
            self.srijan_id = random.randint(1000000000, 9999999999)
            
            # यह सुनिश्चित करने के लिए कि ID वाकई यूनिक है
            while User.objects.filter(srijan_id=self.srijan_id).exists():
                self.srijan_id = random.randint(1000000000, 9999999999)
        
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}  "
    

class SrijanApp(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
    
class SrijanModule(models.Model):
    name = models.CharField(max_length=100)
    app = models.ForeignKey(SrijanApp, on_delete=models.SET_NULL, null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} {self.app}"

class Sample(models.Model):
    first_name = models.CharField(max_length=100)        
    last_name = models.CharField(max_length=100)        

    def __str__(self):
        return f"{self.first_name}"