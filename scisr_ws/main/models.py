from django.db import models

class Event(models.Model):
    number      = models.IntegerField()
    title       = models.CharField(max_length=200)
    description = models.TextField()
    start_date  = models.DateTimeField()
    end_date    = models.DateTimeField()
