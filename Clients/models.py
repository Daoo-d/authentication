from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

# Create your models here.
class Client(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="clients")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="clients")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
