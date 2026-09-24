from django.contrib import admin
from .models import Message, NotificationCategory, Notification, PageVisit
from .models import SystemSetting, Tehsil, TouristPlace, UserAppCategory, UserApp, Webpage
from .models import Location , Contact
# Register your models here.

class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "mobile", "message")

class NotificationCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_hi", "name_en", "description_hi", "description_en")

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("name_hi", "name_en", "description_hi", "description_en")

class PageVisitAdmin(admin.ModelAdmin):
    list_display = ("page_url", "visit_count", "last_visited")

class SystemSettingAdmin(admin.ModelAdmin):
    list_display = ("name_hi", "name_en", "email", "contact", "status")

class TehsilAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en")

class TouristPlaceAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class UserAppCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class UserAppAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")


class WebpageAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class LocationAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("district_hi", "tehsil_en", "gram_panchayat_en", "village_en", "status")

class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "message")

admin.site.register(Message, MessageAdmin)
admin.site.register(NotificationCategory, NotificationCategoryAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(PageVisit, PageVisitAdmin)
admin.site.register(SystemSetting, SystemSettingAdmin)
admin.site.register(Tehsil, TehsilAdmin)
admin.site.register(TouristPlace, TouristPlaceAdmin)
admin.site.register(UserAppCategory, UserAppCategoryAdmin)
admin.site.register(UserApp, UserAppAdmin)
admin.site.register(Webpage, WebpageAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)
