from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from basketballs.models import team


class TeamUser(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="team_user")
    team_id = models.ForeignKey(team.Team, on_delete=models.CASCADE, related_name="team")

    def __unicode__(self):
        return self.name
