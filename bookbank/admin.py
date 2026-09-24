from django.contrib import admin
from .models import Category, BookBankList, BookIssueReturn

# Register your models here.
class BookBankListAdmin(admin.ModelAdmin):
    readonly_fields = ("created_at", "updated_at")
    list_display = ("title", "author", "isbn", "publisher", "status")

admin.site.register(BookBankList, BookBankListAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "created_at", "updated_at")

admin.site.register(Category, CategoryAdmin)

class BookIssueReturnAdmin(admin.ModelAdmin):
    list_display = ("book", "takenby", "bookstatus")

admin.site.register(BookIssueReturn, BookIssueReturnAdmin)
