from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    dates = models.DateField()
    description = models.CharField(max_length=250)
