from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from basketballs.models import team

STATUS = [('extra', 'Extra'), ('squad', 'Squad')]


class Player(models.Model):
    height = models.IntegerField()
    participation = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="player")
    team_id = models.ForeignKey(team.Team, on_delete=models.CASCADE, related_name="player_team")

    @property
    def avg_score(self):
        avg_score = 0
        return avg_score

    def __unicode__(self):
        return self.user_id.first_name + ' ' + self.user_id.last_name
