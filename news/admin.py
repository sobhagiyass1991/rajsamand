from django.contrib import admin
from .models import Category, NewsList

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("name_en", "status")

admin.site.register(Category, CategoryAdmin)

class NewsListAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("title", "status")

admin.site.register(NewsList, NewsListAdmin)
