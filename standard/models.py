from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    pass



class userFiles(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    userName = models.CharField(max_length=100)
    file = models.FileField()
    file_name = models.CharField(max_length=100)
    desc = models.TextField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)


def __str__(self):
    return self.text
