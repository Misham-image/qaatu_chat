from django.db import models
"""
class student(models.Model):
    name =models.CharField(max_length=50)
    age = models.IntegerField()
student = student(name="orange",age=25)


student.save()
"""

class contact(models.Model):
    name =models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=50)
    Message =models.CharField(max_length=50)

# Create your models here.
