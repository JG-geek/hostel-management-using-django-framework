from django.contrib import admin

# Register your models here.
from .models import student_details,hostel_rooms
admin.site.register(student_details)
admin.site.register(hostel_rooms)
