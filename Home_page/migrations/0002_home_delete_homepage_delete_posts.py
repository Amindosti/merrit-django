# Generated by Django 4.1 on 2022-09-07 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_page', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20, null=True)),
                ('Date_Time', models.DateTimeField(auto_now=True)),
                ('form_array', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
    ]
