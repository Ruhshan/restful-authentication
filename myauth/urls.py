from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token
from .api import CreateUserApi, LogInApi, LogOutApi

urlpatterns = [
    url(r'^register/', CreateUserApi.as_view()),
    url(r'^login/', LogInApi.as_view()),
    url(r'^logout/', LogOutApi.as_view()),
]