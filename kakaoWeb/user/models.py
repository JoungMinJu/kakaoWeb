from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, nickname, password, age):
        user = self.model(
            username = username,
            nickname = nickname,
            age=age,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password, nickname=''):
        user = self.create_user(
            username = username,
            nickname = '',
            age =0,
            password = password,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_superuser=True
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=50, unique=True, default ='')
    #아이디
    nickname =models.CharField(max_length = 100, unique=True, default='')
    #닉네임
    age  = models.PositiveIntegerField(default=0)
    #나이

    objects=UserManager()
    is_active =models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD ='username'
    REQUIRED_FIELDS = ['nickname']

    def __str__(self):
        return self.username

