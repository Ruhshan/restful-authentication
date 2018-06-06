from django.contrib import admin

# Register your models here.
from .models import MySession

admin.site.register(MySession)