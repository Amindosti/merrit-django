# Generated by Django 4.1 on 2022-09-03 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0005_createform_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createform',
            old_name='form_name',
            new_name='name',
        ),
    ]
