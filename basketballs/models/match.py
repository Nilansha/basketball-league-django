from django.conf import settings
from django.db import models
from django.utils import timezone

STATUS = [('live', 'Live'), ('finished', 'Finished'), ('yet_to_go', 'Yet to Go'),
          ('canceled', 'Canceled')]


class Match(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(choices=STATUS, max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    datetime = models.DateTimeField()

    def __unicode__(self):
        return self.name
