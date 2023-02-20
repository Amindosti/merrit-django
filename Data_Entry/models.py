from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from djmoney.models.fields import MoneyField
from django.contrib.auth.models import User


class DataEntry(models.Model):
    form_name = models.CharField(max_length=20)
    Textarea = models.TextField(blank=True, null=True)
    Text_field = models.TextField(max_length=10, blank=True, null=True)
    Check_Box = models.BooleanField(blank=True, null=True)
    Password = models.CharField(max_length=25, blank=True, null=True)
    Number = models.IntegerField(blank=True, null=True)
    Url = models.URLField(blank=True, null=True)
    Phone_number = PhoneNumberField(blank=True, null=True)
    Address = models.CharField(max_length=20, blank=True, null=True)
    Date_Time = models.DateTimeField(auto_now=True)
    email_field = models.EmailField(blank=True, null=True)
    document = models.FileField(upload_to='documents/')
    upload_at = models.DateTimeField(auto_now_add=True)
    Currency = MoneyField(max_digits=14, decimal_places=2, default_currency='USD', blank=True, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=25)

    def __str__(self):
        return self.form_name
