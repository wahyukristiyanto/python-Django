from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField()
    description = models.CharField(max_length=256)
    url = models.URLField(blank=True)

    # no need to make migrations if it just methods
    def __str__(self):
        return self.title