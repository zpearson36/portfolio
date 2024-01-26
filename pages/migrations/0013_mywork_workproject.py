# Generated by Django 5.0.1 on 2024-01-26 21:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_myinfo_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WorkProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=256)),
                ('description', models.TextField(default='')),
                ('job_foreign_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.mywork')),
            ],
        ),
    ]