from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    author = models.CharField(max_length=20, null=True)
    Date_Time = models.DateTimeField(auto_now=True)
    form_array = models.CharField(max_length=1000, blank=True, null=True)


