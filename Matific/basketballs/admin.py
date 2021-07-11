from django.contrib import admin
from .models import team,player,match,match_detail,player_point
# Register your models here.

admin.site.register(team.Team)
admin.site.register(player.Player)
admin.site.register(match.Match)
admin.site.register(match_detail.MatchDetail)
admin.site.register(player_point.PlayerPoint)