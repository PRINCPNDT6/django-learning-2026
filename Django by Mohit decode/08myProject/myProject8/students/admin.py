from django.contrib import admin
from students.models import Student, Review
# Register your models here.
# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','age', 'Course', 'roll_no')
    list_filter = ('name', 'roll_no')
    search_fields = ('name', 'roll_no')
    ordering = ('roll_no',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating','review_text', 'name' )
    pass