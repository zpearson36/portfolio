# Generated by Django 5.0.1 on 2024-01-19 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_alter_project_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='text',
            new_name='brief_description',
        ),
        migrations.AddField(
            model_name='project',
            name='detailed_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='project',
            name='specific_lesson',
            field=models.TextField(default=''),
        ),
    ]