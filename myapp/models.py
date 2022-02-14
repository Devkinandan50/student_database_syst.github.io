from django.db import models

# Create your models here.
class Studentdata(models.Model):
    studentname=models.CharField(max_length=50)
    studentcollege=models.CharField(max_length=100)
    studentrollnumber=models.IntegerField()
    studentbranch=models.CharField(max_length=50)
