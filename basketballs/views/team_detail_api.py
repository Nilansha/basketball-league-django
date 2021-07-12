from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from basketballs.permissions import IsCoach, IsLeagueAdmin
from rest_framework.status import (
    HTTP_200_OK
)
from rest_framework.response import Response
from basketballs import models
from django.shortcuts import get_object_or_404


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsCoach,))
def get_all_team_players(request):
    if request.user.groups.filter(name='Admin') or request.user.is_superuser:
        players = models.player.Player.objects.filter().values()
    else:
        team = models.team.Team.objects.filter(coach_id=request.user.id)
        # TODO: if coach has no team
        players = models.player.Player.objects.filter(team_id=team[0].id).values()
    player_list = []
    for ply in players:
        player = get_object_or_404(models.player.Player, pk=ply['id'])
        participation = get_player_match_count(player)
        avg_score = get_player_avg_score(player, participation)
        rec = {'id': player.id, 'name': player.user_id.first_name+' ' + player.user_id.last_name,'team':player.team_id.name,
               'height': player.height, 'participation': participation, 'avg_score': avg_score}
        player_list.append(rec)
    return Response(player_list, status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsCoach,))
def get_player(request, pk):
    team = models.team.Team.objects.get(coach_id=request.user.id)
    player = get_object_or_404(models.player.Player, pk=pk)
    if team.id != player.team_id.id:
        return Response({'error': "This player is not belong to your team"}, status=HTTP_200_OK)
    participation = get_player_match_count(player)
    avg_score = get_player_avg_score(player, participation)
    rec = {'id': player.id, 'name': player.user_id.first_name+' ' + player.user_id.last_name,
           'height': player.height, 'participation': participation, 'avg_score': avg_score}
    return Response(rec, status=HTTP_200_OK)


def get_player_match_count(player):
    matches = len(models.player_point.PlayerPoint.objects.filter(player_id=player.id).values_list('id', flat=True))
    return matches


def get_player_avg_score(player, participation):
    score = sum(models.player_point.PlayerPoint.objects.filter(player_id=player.id).values_list('points', flat=True))
    if participation == 0:
        avg = 0
    else:
        avg = score/participation
    return avg


@csrf_exempt
@api_view(["GET"])
@permission_classes((IsCoach,))
def get_top_players_with_ranks(request):
    team_coach = models.team.Team.objects.filter(coach_id=request.user.id)
    players = models.player.Player.objects.filter(team_id=team_coach[0].id).values()
    player_list = []

    for ply in players:
        player = get_object_or_404(models.player.Player, pk=ply['id'])
        participation = get_player_match_count(player)
        avg_score = get_player_avg_score(player, participation)
        rec = {'id': player.id, 'name': player.user_id.first_name + ' ' + player.user_id.last_name,
               'avg_score': avg_score}
        # if avg_score is grater than 90
        if avg_score > 90:
            player_list.append(rec)

    sorted_players = sorted(player_list, key=lambda x: (int(player_list[0]['avg_score'])))
    count = 1
    for player in sorted_players:
        player.update({'rank': count})
        count += 1

    return Response(player_list, status=HTTP_200_OK)

