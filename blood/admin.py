from django.contrib import admin
from .models import Donor, Donation, Requestt

# Register your models here.
class DonorAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "blood_group", "created_at", "updated_at", "created_by")
admin.site.register(Donor, DonorAdmin)

# Register your models here.
class DonationAdmin(admin.ModelAdmin):
    list_display = ("id", "donorname",  "blood_group", "volume", "created_at", "updated_at", "created_by")
admin.site.register(Donation, DonationAdmin)

# Register your models here.
class RequesttAdmin(admin.ModelAdmin):
    list_display = ("id", "patientname", "volume", "created_at", "updated_at", "created_by")
admin.site.register(Requestt, RequesttAdmin)

