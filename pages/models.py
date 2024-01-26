from cloudinary.models import CloudinaryField
from django.db import models


class Project(models.Model):
    name                 = models.CharField(max_length=100)
    image                = CloudinaryField('image')
    brief_description    = models.TextField(default="")
    link                 = models.URLField(default="#")
    detailed_description = models.TextField(default="")
    specific_lesson      = models.TextField(default="")

class MyInfo(models.Model):
    first_name   = models.CharField(max_length=30)
    last_name    = models.CharField(max_length=30)
    location     = models.CharField(max_length=100)
    email        = models.EmailField(max_length=128)
    linked_in    = models.URLField(max_length=500)
    github       = models.URLField(max_length=500)
    itch_io      = models.URLField(max_length=500)
    image        = CloudinaryField('image')
    introduction = models.TextField(default="Hello There")

class MyWork(models.Model):
    company    = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date   = models.DateField()
    title      = models.CharField(max_length=100)

class WorkProject(models.Model):
    job_foreign_key = models.ForeignKey(MyWork, on_delete=models.CASCADE)
    heading         = models.CharField(max_length=256)
    description     = models.TextField(default="")
