# Generated by Django 3.2.5 on 2021-08-24 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_contactus_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='user',
        ),
    ]
