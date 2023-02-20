from django.db import models
from django.contrib.auth.models import User


class CreateForm(models.Model):
    author = models.CharField(max_length=20, null=True)
    Date_Time = models.DateTimeField(auto_now=True)
    formarray = models.CharField(max_length=100, blank=True)



