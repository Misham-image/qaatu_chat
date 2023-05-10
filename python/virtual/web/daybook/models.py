from django.db import models
<<<<<<< HEAD
from django.contrib.auth.models import User

class userdetails(models.Model):
    
    name=models.CharField(max_length=100)
    mobile=models.CharField(max_length=100)
    email=models.EmailField()
    password=models.CharField(max_length=100)
    confirm=models.CharField(max_length=100)

class journels(models.Model):
    user1 = models.OneToOneField(User,on_delete=models.CASCADE)
=======

class journels(models.Model):

>>>>>>> 84c433cfe5ad37f25de32811fd85868ff851981f
    Products = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    Invoice = models.IntegerField()
    Date = models.DateField()


    class Meta:

        ordering =['Date']