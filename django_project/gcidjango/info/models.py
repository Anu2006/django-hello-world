from django.db import models


class GetInfo(models.Model):
    name = models.CharField(max_length=200, default='')
    age = models.IntegerField(default='')
    birthday = models.DateField(default='2006-01-03')
    country = models.CharField(max_length=20, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default='')
    school = models.CharField(blank=True, max_length=200, default='')
    over_18 = models.BooleanField(default=True)
