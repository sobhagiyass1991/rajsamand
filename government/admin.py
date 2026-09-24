from django.contrib import admin
from .models import SchemeCategory, Scheme
# Register your models here.
class SchemeCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class SchemeAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "slug", "status")

admin.site.register(SchemeCategory, SchemeCategoryAdmin)
admin.site.register(Scheme, SchemeAdmin)
