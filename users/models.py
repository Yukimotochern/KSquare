from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    objects = CustomUserManager()


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


