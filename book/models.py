from django.db import models

from event.models import Event


# Create your models here.
class BookInfo(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    past_theme = models.CharField(max_length=255)
    introduction = models.TextField()
    def __str__(self):
        return self.event.name