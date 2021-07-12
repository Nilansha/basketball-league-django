from django.db import models
from django.utils import timezone
from basketballs.models import player, match
TYPE = [('goal', 'Goal'), ('assist', 'Assist'), ('block', 'Block')]


class PlayerPoint(models.Model):
    type = models.CharField(choices=TYPE, max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    player_id = models.ForeignKey(player.Player, on_delete=models.CASCADE)
    match_id = models.ForeignKey(match.Match, on_delete=models.CASCADE)
    points = models.IntegerField()
