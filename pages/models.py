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
