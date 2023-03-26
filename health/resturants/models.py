from django.db import models

# Create your models here.
class Resturants(models.Model):
    title=models.CharField(max_length=200)
    phoneNumber=models.CharField(max_length=200,null=True)
    address=models.CharField(max_length=200)
    lat=models.CharField(max_length=200)
    lon=models.CharField(max_length=200)
    description=models.TextField(max_length=500,null=True)
    opening_hours=models.TextField(max_length=500 ,null=True)
    whatsappNumber=models.CharField(max_length=200,null=True)
    facebookLink=models.CharField(max_length=200,null=True)
    instagramLink=models.CharField(max_length=200,null=True)




    def __str__(self):
        return f"{self.title}"


