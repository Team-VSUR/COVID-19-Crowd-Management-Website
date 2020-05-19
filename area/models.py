from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TYPE_CHOICES = (
    ('RED', 'Red'),
    ('Orange', 'Orange'),
    ('Green', 'Green'),
)

class Area(models.Model):
    name = models.CharField(max_length=50)
    zone= models.CharField(max_length=10,choices=TYPE_CHOICES)
    def __str__(self):
        return self.name
