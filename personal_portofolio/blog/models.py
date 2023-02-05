from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    description = models.CharField(max_length=100)
    url = models.URLField(blank=True)