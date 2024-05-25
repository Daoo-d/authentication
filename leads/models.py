from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Lead(models.Model):
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
        (LOW,'low'),
        (MEDIUM,'medium'),
        (HIGH,'high'),
    )
    NEW = 'new'
    CONTACTED = 'contacted'
    WON = 'won'
    LOST = 'lost'

    CHOICES_STATUS = (
        (NEW, 'new'),
        (CONTACTED, 'contacted'),
        (WON, 'won'),
        (LOST, 'lost')
    )

    priority = models.CharField(max_length=10,choices=CHOICES_PRIORITY,default=MEDIUM)
    status = models.CharField(max_length=10,choices=CHOICES_STATUS,default=NEW)
