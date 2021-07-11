from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=200)
    win_count = models.IntegerField()
    lost_count = models.IntegerField()
    draw_count = models.IntegerField()
    avg_score = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)
    coach_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="coach")

    def __unicode__(self):
        return self.name
