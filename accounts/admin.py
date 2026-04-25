from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, SrijanApp, SrijanModule, Sample, Role

class UserAdmin(admin.ModelAdmin):
    #readonly_fields = ("created_at", "updated_at")
    list_display = ("first_name", "last_name", "username", "email")

class SrijanAppAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")

class SrijanModuleAdmin(admin.ModelAdmin):
    list_display = ("id",  "app", "name", "created_at", "updated_at")

class SampleAdmin(admin.ModelAdmin):
    list_display = ("id",  "first_name", "last_name")

class RoleAdmin(admin.ModelAdmin):
    list_display = ("id",  "name")

admin.site.register(User, UserAdmin) 
admin.site.register(SrijanApp, SrijanAppAdmin) 
admin.site.register(SrijanModule, SrijanModuleAdmin) 
admin.site.register(Sample, SampleAdmin) 
admin.site.register(Role, RoleAdmin) 
