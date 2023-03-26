from django.db import models

# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=200)
    telephone_number=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200)
    locations=models.CharField(max_length=200)
    features=models.TextField(max_length=500,null=True)
    opening_hours=models.TextField(max_length=500 ,null=True)
    # categories

    def __str__(self):
        return f"{self.name}"


