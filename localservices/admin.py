from django.contrib import admin
from .models import LssemsService, ServiceProvider

class LssemsServiceAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "name", "status")

class ServiceProviderAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "name", "status")

admin.site.register(LssemsService, LssemsServiceAdmin)
admin.site.register(ServiceProvider, ServiceProviderAdmin)
