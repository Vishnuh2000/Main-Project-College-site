# Generated by Django 3.2.4 on 2021-06-22 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0006_rename_facilities_image_facilities_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Teachers Name')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('Email', models.EmailField(max_length=254, unique=True, verbose_name='Eamil Address')),
                ('Phone', models.IntegerField(verbose_name='Phone Number')),
                ('T_image', models.ImageField(upload_to='', verbose_name='Teacher image')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('Name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='owner.department', verbose_name='Department Name')),
            ],
        ),
    ]
