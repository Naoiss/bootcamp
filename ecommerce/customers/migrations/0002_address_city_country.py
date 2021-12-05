# Generated by Django 3.2.9 on 2021-12-05 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'country',
                'verbose_name_plural': 'countries',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(max_length=35, verbose_name='name')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='Modified at')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('fullname', models.CharField(max_length=255, verbose_name='Full Name')),
                ('line1', models.CharField(max_length=255, verbose_name='Address Line 1')),
                ('line2', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address Line 2')),
                ('phone', models.CharField(max_length=255, verbose_name='Phone')),
                ('district', models.CharField(max_length=255, verbose_name='District')),
                ('postcode', models.CharField(max_length=255, verbose_name='Post Code')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customers.city', verbose_name='City')),
            ],
            options={
                'verbose_name': 'address',
                'verbose_name_plural': 'addresses',
            },
        ),
    ]
