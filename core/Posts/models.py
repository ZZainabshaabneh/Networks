from django.db import models

from django.db import models
from django.contrib.auth.models import User,Address

class Posts(models.Model):
    text = models.CharField(max_length=100, blank=False)
    image =models.ImageField(default='default.png',blank=True)
    #posts = models.BigIntegerField(auto_created=True,unique=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.ForeignKey(Address,on_delete=models.CASCADE)


class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE)


class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE)
    text_comment =models.CharField(max_length=100, blank=False)
    