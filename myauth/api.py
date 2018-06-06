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


class LogOutApi(JSONWebTokenAPIView):
    """
    API View that checks the validity of a token, user in the token then deletes the corresponding session
    object if the user is logged in.

    Returns appropiate message for action.
    """
    def post(self, request):
        token = request.data['token'] 
        msg = _("User is logged out")

        #checking token's validity
        try:
            payload = jwt_decode_handler(token)
        except jwt.ExpiredSignature:
            msg = _('Signature has expired.')
            
        except jwt.DecodeError:
            msg = _('Error decoding signature.')
        
        #checking username in both user model and session
        try:
            username = jwt_get_username_from_payload(payload)

            if not username:
                msg = _('Invalid payload.')
                raise serializers.ValidationError(msg)

            # Make sure user exists
            try:
                user = User.objects.get_by_natural_key(username)
            except User.DoesNotExist:
                msg = _("User doesn't exist.")
            
            if not user.is_active:
                msg = _('User account is disabled.')

            
            if MySession.objects.filter(username = user.username).exists():
                MySession.objects.filter(username = user.username).delete()
                msg = _("User is logged out")
            else:
                msg = _("User is was not logged on")
        except:
            pass
    

        return Response(msg)

    