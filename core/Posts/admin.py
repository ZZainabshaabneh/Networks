from django.contrib import admin
from .models import Like,Posts,User,Comment,Address
admin.site.register(Posts)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(Address)
admin.site.register(User)

