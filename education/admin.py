from django.contrib import admin
from .models import Teacher, Subject, ClassSection, School, Student, SubjectMark

class SubjectAdmin(admin.ModelAdmin):
    list_display = ("id",  "name")

class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "child", "get_subject")

    @admin.display(empty_value="unknown")
    def get_subject(self, obj):
        return obj.subject

class ClassSectionAdmin(admin.ModelAdmin):
    list_display = ("id",  "name")

class SchoolAdmin(admin.ModelAdmin):
    list_display = ("id",  "school_name")

class StudentAdmin(admin.ModelAdmin):
    list_display = ("id",  "child", "father_name")

class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ("id",  "child", "total")

    @admin.display(description="Total")
    def totalmarks(self, obj):
        return f"{obj.first}+{obj.second}+{obj.third}"


