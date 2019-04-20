from django.db import models
from django.utils import timezone
from django.conf import settings
from bugs.models import Bugs

from django.contrib.auth.models import User

# Create your models here.

class Comments(models.Model):
    
    
    username = models.CharField(max_length=30,default=User )
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True )
    bug_id = models.ForeignKey(Bugs, on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    likes = models.IntegerField(default=0)
    
    
    

    def __str__(self):
        return self.username
        

