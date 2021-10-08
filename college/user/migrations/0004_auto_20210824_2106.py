# Generated by Django 3.2.5 on 2021-08-24 15:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_remove_contactus_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='email',
        ),
        migrations.AddField(
            model_name='contactus',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.user'),
            preserve_default=False,
        ),
    ]
