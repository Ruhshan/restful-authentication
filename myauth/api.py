from rest_framework import permissions
from rest_framework import serializers

from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, JSONWebTokenSerializer
from rest_framework_jwt.views import JSONWebTokenAPIView
import jwt
from django.utils.translation import ugettext as _
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import MySession


class CreateUserApi(CreateAPIView):
    """
    API View that receives a POST with a username, password, email, first_name, last_name.

    Returns a JSON Web Token with given values along with id and password hash
    """
    model = User
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


class LogInApi(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = JSONWebTokenSerializer


class LogOutApi(APIView):
    def post(self, request):
        user = request.data['user']
        if MySession.objects.filter(username = user).exists():
                MySession.objects.filter(username = user).delete()
                msg = _("User is logged out")
        else:
            msg = _("User is was not logged on")
        
        return Response(msg)
    