from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK
)
from rest_framework.response import Response
from basketballs import models

'''
Match Details Feature
Access : Admin, Coach, Player
api : /api/match_details
'''
@csrf_exempt
@api_view(["GET"])
@permission_classes((IsAuthenticated, ))
def match_details(request):
    matches = models.match.Match.objects.all().values()
    match_list = []
    for match in matches:
        # get teams using match
        teams = models.match_detail.MatchDetail.objects.all().filter(match_id=match['id'])
        team_list = []
        for team in teams:
            rec_team = {"name": team.team_id.name, "score": team.score, "status": team.status}
            team_list.append(rec_team)
        rec = {"name": match['name'], "description": match['description'], "date": match['datetime'],
               "status": match["status"], "teams": team_list}
        match_list.append(rec)
    return Response(match_list, status=HTTP_200_OK)

