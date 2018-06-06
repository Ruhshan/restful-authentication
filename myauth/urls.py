from django.conf.urls import url
from .api import CreateUserApi, LogInApi, LogOutApi

urlpatterns = [
    url(r'^register/', CreateUserApi.as_view()),
    url(r'^login/', LogInApi.as_view()),
    url(r'^logout/', LogOutApi.as_view()),
]