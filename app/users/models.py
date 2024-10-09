from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    status = models.BooleanField(blank=True, null=True)
    
    class Meta:
        db_table = 'User'
        
    def __str__(self):
        return self.username
