from django.contrib import admin
from .models import UtilityCategory, Utility

# Register your models here.
class UtilityCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class UtilityAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("category", "name_hi", "name_en", "description_hi", "description_en", "status")

admin.site.register(UtilityCategory, UtilityCategoryAdmin)
admin.site.register(Utility, UtilityAdmin)
