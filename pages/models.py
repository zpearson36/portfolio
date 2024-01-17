from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "images/")
    text = models.TextField()
