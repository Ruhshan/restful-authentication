from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .api import CreateUserView, ObtainJSONWebToken, LogOutApi

urlpatterns = [
    url(r'^register/', CreateUserView.as_view()),
    url(r'^login/', ObtainJSONWebToken.as_view()),
    url(r'^logout/', LogOutApi.as_view()),
]