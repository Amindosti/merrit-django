# Generated by Django 4.1 on 2022-09-07 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0002_post_delete_dashboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='writer',
        ),
    ]
