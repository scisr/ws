from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description=models.TextField()
    time_start=models.DateTimeField()
    time_end=models.DateTimeField()
