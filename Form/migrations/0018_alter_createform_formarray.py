# Generated by Django 4.1 on 2022-09-30 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Form', '0017_remove_createform_kone_sefid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createform',
            name='formarray',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]