from django.contrib import admin
from .models import AccountType, Message, NotificationCategory, Notification, PageVisit,  RecruitmentCategory, Recruitment
from .models import SchemeCategory, Scheme, SystemSetting, Tehsil, TouristPlace, UserAppCategory, UserApp, UtilityCategory, Utility, Webpage
from .models import Location , Contact, Venue, LssemsService, ServiceProvider
# Register your models here.
class AccountTypeAdmin(admin.ModelAdmin):
    fields = ("name_hi", "name_en", "description_hi", "description_en", "status", "created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class MessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "mobile", "message")

class NotificationCategoryAdmin(admin.ModelAdmin):
    list_display = ("name_hi", "name_en", "description_hi", "description_en")

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("name_hi", "name_en", "description_hi", "description_en")

class PageVisitAdmin(admin.ModelAdmin):
    list_display = ("page_url", "visit_count", "last_visited")

    
class RecruitmentAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class RecruitmentCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class SchemeCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class SchemeAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "slug", "status")

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

class UtilityCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class UtilityAdmin(admin.ModelAdmin):
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

class VenueAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class LssemsServiceAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "name", "status")

class ServiceProviderAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("id", "name", "status")

admin.site.register(AccountType, AccountTypeAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(NotificationCategory, NotificationCategoryAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(PageVisit, PageVisitAdmin)
admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(RecruitmentCategory, RecruitmentCategoryAdmin)
admin.site.register(SchemeCategory, SchemeCategoryAdmin)
admin.site.register(Scheme, SchemeAdmin)
admin.site.register(SystemSetting, SystemSettingAdmin)
admin.site.register(Tehsil, TehsilAdmin)
admin.site.register(TouristPlace, TouristPlaceAdmin)
admin.site.register(UserAppCategory, UserAppCategoryAdmin)
admin.site.register(UserApp, UserAppAdmin)
admin.site.register(UtilityCategory, UtilityCategoryAdmin)
admin.site.register(Utility, UtilityAdmin)
admin.site.register(Webpage, WebpageAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(LssemsService, LssemsServiceAdmin)
admin.site.register(ServiceProvider, ServiceProviderAdmin)
