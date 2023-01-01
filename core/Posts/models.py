from django.db import models

from django.db import models

from core.Users.models import Address
from core.Users.models import User

class Posts(models.Model):
    text = models.CharField(max_length=100, blank=False)
    image =models.ImageField(default='default.png',blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='UserPosts')
    address = models.ForeignKey(Address,on_delete=models.CASCADE, related_name='UserAddress')


class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE)


class Comment(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    posts = models.ForeignKey(Posts,on_delete=models.CASCADE)
    text_comment =models.CharField(max_length=100, blank=False)
    