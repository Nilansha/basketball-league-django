from django.urls import path, include
from basketballs import views
urlpatterns = [
    path('login', views.login_api.user_login),
    path('logout', views.login_api.user_logout),
    path('match_details', views.match_details_api.match_details),
    path('team_players', views.team_detail_api.get_all_team_players),
    path('player/<int:pk>', views.team_detail_api.get_player),
    path('top_players', views.team_detail_api.get_top_players_with_ranks),
]
