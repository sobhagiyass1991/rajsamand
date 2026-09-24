from django.contrib import admin
from .models import RecruitmentCategory, Recruitment, Jobslist

class RecruitmentAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class RecruitmentCategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_hi", "name_en", "description_hi", "description_en", "status")

class JobslistAdmin(admin.ModelAdmin):
    list_display = ("id",  "postname")


admin.site.register(Recruitment, RecruitmentAdmin)
admin.site.register(RecruitmentCategory, RecruitmentCategoryAdmin)
admin.site.register(Jobslist, JobslistAdmin) 


