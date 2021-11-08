from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatares/', default='avatares/logouser.jpg')
    desc = models.TextField(null=True, blank=True)
    num_tel = models.CharField(max_length = 20, null=True, blank=True)
    pais = models.CharField(max_length = 30)
    fecha_nac = models.DateField(default="2018-07-22")
    tipo_us = models.CharField(max_length = 30, default="normal")
    def __str__(self):
         return "{}".format(self.username)