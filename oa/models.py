from django.db import models


class UserInfoModel(models.Model):
    userId = models.CharField(max_length=100, unique=tuple, null=False, blank=False)
    userName = models.CharField(max_length=100,  unique=True, null=False, blank=False)
    userPwd = models.CharField(max_length=100, null=False, blank=False)
    userPhone = models.CharField(max_length=30, default='')
    userStatus = models.IntegerField(default=0)


