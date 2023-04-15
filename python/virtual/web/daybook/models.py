from django.db import models

class journels(models.Model):

    Products = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    Invoice = models.CharField(max_length=50)
    Date = models.DateField()


    class Meta:

        ordering =['Date']