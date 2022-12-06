from django.db import models
from django.contrib.auth.models import posts
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, blank=False,null=False)
    email = models.CharField(max_length=100, blank=False,null=False)
    password =models.CharField(max_length=50,blank=False,unique=False)
    first_name =models.CharField(max_length=100, blank=False,null=False)
    last_name =models.CharField(max_length=100, blank=False,null=False)
    mobile =models.BigIntegerField(unique=True ,blank=True,null=True)



class Address(models.Model):
    country =models.CharField(max_length=100,blank=True,null=True)
    city =models.CharField(max_length=100,blank=True,null=True)
    street =models.CharField(max_length=100, blank=True, default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)

class Relation(models.Model):
    relation_type =models.CharField(max_length=100,blank=False)
    status =models.CharField(unique=False,max_length=100,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE)

