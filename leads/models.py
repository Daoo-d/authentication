from django.db import models
from django.contrib.auth.models import User
from teams.models import Team

# Create your models here.
class Lead(models.Model):
    team = models.ForeignKey(Team,on_delete=models.CASCADE,related_name="leads")
    name = models.CharField(max_length=255)
    email = models.EmailField()
    description = models.TextField(blank=True,null=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name="leads")
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'

    CHOICES_PRIORITY = (
        ('low','LOW'),
        ('medium','MEDIUM'),
        ('high','HIGH'),
    )
    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
        ('new', 'New'),  
        ('contacted', 'Contacted'),
        ('won', 'Won'),
        ('lost', 'Lost'),
    )

    priority = models.CharField(max_length=10,choices=CHOICES_PRIORITY,default=MEDIUM)
    status = models.CharField(max_length=10,choices=CHOICES_STATUS,default=NEW)
    convertd_to_client = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        
    def __str__(self):
        return self.name
    
