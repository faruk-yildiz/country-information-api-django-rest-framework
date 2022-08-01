from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100)
    isoCode=models.CharField(max_length=10)
    callingCode=models.CharField(max_length=10)
    flag=models.CharField(max_length=300)
    capital=models.CharField(max_length=50)
    population=models.IntegerField()

    def __str__(self):
        return self.name
