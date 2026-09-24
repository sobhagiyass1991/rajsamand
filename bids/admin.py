from django.contrib import admin
from .models import Product, Sample

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ["randomid"]
    list_display  = ["id", "title", "status", "created_at", "updated_at"]

class SampleAdmin(admin.ModelAdmin):
    list_display = ["id", "integer", "float", "duration"]

admin.site.register(Product, ProductAdmin)
admin.site.register(Sample, SampleAdmin)