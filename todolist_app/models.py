from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TodoList(models.Model):
    Manager = models.ForeignKey(User, on_delete = models.CASCADE, default = None )
    Task = models.CharField(max_length=200)
    Done = models.BooleanField(default = False)
    
    def __str__(self):
        return self.Task + '-' + str(self.Done)
    
    