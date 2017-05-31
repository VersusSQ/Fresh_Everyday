from django.db import models

# Create your models here.

class UserInfoManager(models.Manager):
    def get_queryet(self):
        return super(UserInfoManager, self).get_queryset().filter(isdelete=False)

    def create(self, name, pwd, email):
        user = UserInfo()
        user.uName = name
        user.uPasswd = pwd
        user.uEmail = email
        return user


class UserInfo(models.Model):
    uName = models.CharField(max_length=20)
    uPasswd = models.CharField(max_length=20)
    uEmail = models.CharField(max_length=30)
    uShou = models.CharField(max_length=50, default='')
    uAddr = models.CharField(max_length=50, default='')
    uTel = models.CharField(max_length=20, default='')
    uYoubian = models.CharField(max_length=6, default='')
    isdelete = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_info'

    users = UserInfoManager()

