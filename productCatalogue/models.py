from django.db import models

"""
city:string
rooms:int
rent:int
postedDate:int(unix timestamp)
"""

# Create your models here.
class Product(models.Model):
    #Debugging field
    apartmentName=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    rooms=models.IntegerField()
    rent=models.IntegerField()
    postedDate=models.IntegerField()

    #For Debugging listing 
    def __str__(self):
        return self.apartmentName