from django.contrib import admin
from .models import PropertyList

class PropertyListAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "title", "status")

admin.site.register(PropertyList, PropertyListAdmin)
