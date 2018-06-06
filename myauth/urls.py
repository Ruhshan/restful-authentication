from django.conf.urls import url
from .api import CreateUserView

urlpatterns = [
    url(r'^register/', CreateUserView.as_view()),
]