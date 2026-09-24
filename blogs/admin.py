from django.contrib import admin
from .models import BlogList

# Register your models here.
class BlogListAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("title", "text", "status")

admin.site.register(BlogList, BlogListAdmin)
