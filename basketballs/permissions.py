from rest_framework import permissions
from django.db.models import Q


class IsCoach(permissions.BasePermission):
    def has_permission(self, request, view):
        # if request.user and request.user.groups.filter(name='Coach').filter(name='Admin'):
        if (request.user and request.user.groups.filter(Q(name='Coach') | Q(name='Admin'))) \
                or request.user.is_superuser:  # check logged user is a coach or admin
            return True
        return False


class IsLeagueAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.user and request.user.groups.filter(name='Admin')) \
                or request.user.is_superuser:  # check logged user is an admin
            return True
        return False
