from django.contrib import admin
from .models import Category, ItemList

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at")
admin.site.register(Category, CategoryAdmin)

class ItemListAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at", "updated_at", "category", "mobile", "ownername", "description", "image", "status", "created_by")
admin.site.register(ItemList, ItemListAdmin)
