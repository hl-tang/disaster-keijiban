from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.id} {self.username} {self.is_admin}"
