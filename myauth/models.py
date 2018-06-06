from django.db import models

# Create your models here.
class MySession(models.Model):
    username = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username