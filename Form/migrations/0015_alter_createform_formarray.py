# Generated by Django 4.1 on 2022-09-29 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0014_alter_createform_formarray'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createform',
            name='formarray',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
