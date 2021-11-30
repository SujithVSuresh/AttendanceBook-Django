from django.db import models
from django.db.models.fields import CharField

# Create your models here.
class Class(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=255)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    roll_number = models.IntegerField()

    def __str__(self):
        return str(self.id)

class Attendance(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    is_present = models.ManyToManyField(Student, null=True, blank=True, related_name='is_present')
    is_absent = models.ManyToManyField(Student, null=True, blank=True, related_name='is_absent')
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.class_name) 
