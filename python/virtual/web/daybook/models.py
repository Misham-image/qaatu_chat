from django.db import models

class journels(models.Model):

    Products = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    Invoice = models.IntegerField()
    Date = models.DateField()


    class Meta:

        ordering =['Date']