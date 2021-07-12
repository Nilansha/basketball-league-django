from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_403_FORBIDDEN,
    HTTP_200_OK
)

from django.contrib.auth import logout
from django.contrib.auth import login

from rest_framework.response import Response

'''
Login Feature
Access : Admin, Coach, Player
api : /api/user_login
'''
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny, ))
def user_login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    # validate user name and password
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'}, status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'}, status=HTTP_401_UNAUTHORIZED)
    login(request, user)
    # create token
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'username': user.username, 'token': token.key}, status=HTTP_200_OK)


'''
Logout Feature
Access : Admin, Coach, Player
api : /api/user_logout
'''
@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated, ))
def user_logout(request):
    try:
        request.user.auth_token.delete()
    except (AttributeError, ObjectDoesNotExist) as e:
        raise Exception(e)
    logout(request)
    return Response({"success": "Successfully logged out."}, status=HTTP_200_OK)
