from django.conf import settings
from django.db import models
from django.utils import timezone
from basketballs.models import team, match

STATUS = [('win', 'Win'), ('loss', 'Loss'), ('draw', 'Draw')]


class MatchDetail(models.Model):
    team_id = models.ForeignKey(team.Team, on_delete=models.CASCADE)
    match_id = models.ForeignKey(match.Match, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=100)
    score = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now)

