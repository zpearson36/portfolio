# Generated by Django 5.0.1 on 2024-01-17 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_myinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='myinfo',
            name='introduction',
            field=models.TextField(default='Hello There'),
        ),
    ]