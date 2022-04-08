

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    id = models.CharField(primary_key=True, max_length=20)
    user_name = models.CharField(max_length=20,blank=True,null=True)
    user_pwd = models.CharField(max_length=20,blank=True,null=True)

class UserInfo(models.Model):