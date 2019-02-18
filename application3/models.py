from django.db import models


class Reg(models.Model):
    fname = models.CharField(max_length=20,null=True)
    lname = models.CharField(max_length=20,null=True)
    user = models.CharField(primary_key=True, max_length=20)
    pwd = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20,null=True,unique=True)
    email = models.EmailField(max_length=20, unique=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, blank=True, null=True)




# Create your models here.
