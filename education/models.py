from django.db import models
from django.contrib.auth.models import User
from django.conf import settings 

# Create your models here.
class School(models.Model):
    BOARD_TYPES = [
        ('RBSE','RBSE'),
        ('CBSE','CBSE')
    ]

    school_name = models.CharField(max_length=100)
    address = models.TextField(max_length=512, null=True, blank=True)
    established_year = models.DateField(null=True, blank=True)
    principal_name = models.CharField(max_length=100)
    board = models.CharField(choices=BOARD_TYPES, default='RBSE', max_length=50, null=True, blank=True)
    created_by = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="schoolcreatedby")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.school_name}"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class ClassSection(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

class Teacher(models.Model):
    #academic_session = models.PositiveSmallIntegerField(max_length=4, null=True, blank=True)
    #subject = models.CharField(max_length=50, null=True, blank=True) 
    #class_name = models.CharField(max_length=50, null=True, blank=True) 
    qualification = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(null=True, blank=True)
    salary = models.PositiveIntegerField(null=True, blank=True)
    joining_date = models.DateTimeField(auto_now=True)
    subject = models.ManyToManyField(Subject, related_name="subjects")
    classname = models.ManyToManyField(ClassSection, related_name="classenames")
    child = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="teachercreatedby")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"{self.child.username}"

class Student(models.Model):
    child = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="studentcreatedby")
    classname = models.ManyToManyField(ClassSection, related_name="classename")
    father_name = models.CharField(max_length=100, null=True, blank=True)
    mother_name = models.CharField(max_length=100, null=True, blank=True)
    mobile = models.PositiveIntegerField(null=True, blank=True)
    admission_no = models.PositiveIntegerField(null=True, blank=True)
    admission_date = models.DateTimeField(null=True, blank=True)
    #subject = models.ManyToManyField(Subject, related_name="subjects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
       return f"{self.child.username}"

class SubjectMark(models.Model):
    child = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="subjectmarkcreatedby")
    classname = models.ManyToManyField(ClassSection, related_name="myclassename")
    mobile = models.PositiveIntegerField(null=True, blank=True)
    first = models.SmallIntegerField(null=True, blank=True)
    second = models.SmallIntegerField(null=True, blank=True)
    third = models.SmallIntegerField(null=True, blank=True)
    total = models.SmallIntegerField(null=True, blank=True, default="calculate_total")
    subject = models.ManyToManyField(Subject, related_name="marksubjects")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def calculate_total(self):
        self.total = self.first + self.second + self.third
        return self.total  

    def save(self, *args, **kwargs):
        self.calculate_total()

        super().save(*args, **kwargs)

    def __str__(self):
       return f"{self.child.username} {self.first} {self.second} {self.third} {self.total} "

# User Quiz and Questions , Options models are pending for this Models.
class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_right = models.BooleanField(default=False)
