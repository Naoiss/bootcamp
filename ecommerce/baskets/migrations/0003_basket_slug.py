# Generated by Django 3.2.9 on 2021-12-23 18:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('baskets', '0002_auto_20211205_0953'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='slug',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4),
        ),
    ]
