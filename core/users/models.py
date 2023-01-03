from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, blank=False,null=False)
    email = models.CharField(max_length=100, blank=True,null=False)
    password =models.CharField(max_length=50,blank=False,unique=False)
    first_name =models.CharField(max_length=100, blank=True,null=False)
    last_name =models.CharField(max_length=100, blank=True,null=False)
    mobile =models.BigIntegerField(unique=True ,blank=True,null=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return self.username

class Address(models.Model):
    country =models.CharField(max_length=100,blank=True,null=True)
    city =models.CharField(max_length=100,blank=True,null=True)
    street =models.CharField(max_length=100, blank=True, default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)


class Relation(models.Model):
    relation_type =models.CharField(max_length=100,blank=False)
    status =models.CharField(unique=False,max_length=100,blank=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='User_relation')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE , related_name='receiver_relation')

