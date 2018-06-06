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

from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
jwt_get_username_from_payload = api_settings.JWT_PAYLOAD_GET_USERNAME_HANDLER

from .models import MySession

#from rest_framework_jwt.serializers import JSONWebTokenSerializer

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
    