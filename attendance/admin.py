from django.contrib import admin
from .models import Attendance, Class, Student
# Register your models here.
admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Attendance)