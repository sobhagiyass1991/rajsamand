from django.contrib import admin
from .models import VideoList

# Register your models here.
class VideoListAdmin(admin.ModelAdmin):
    list_display = ("title", "status", "created_at", "updated_at")

admin.site.register(VideoList, VideoListAdmin)