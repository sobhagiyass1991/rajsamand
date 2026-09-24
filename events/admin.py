from django.contrib import admin
from .models import Venue

# Register your models here.
class VenueAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

admin.site.register(Venue, VenueAdmin)
