from django.db import models

class Familiares(models.Model):
    name= models.CharField(max_length=30)
    age = models.IntegerField()
    description=models.CharField(max_length=20)
    creation_date=models.DateField(auto_now_add=True, null=True, blank=True)
    

