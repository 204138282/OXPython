from django.contrib import admin

# Register your models here.
from .models import Student

@admin.register(Student)
class BlogTypeAdmin(admin.ModelAdmin):
	list_display = ('pk', 'name')
		