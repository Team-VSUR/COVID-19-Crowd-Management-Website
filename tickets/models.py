from django.db import models

# Create your models here.

def crowd(value):
    if value>10:
        raise ValidationError("Crowd Limit Exceeded!")

def twelvedigit(value):
    count = 0
    while value != 0:
        value //= 10
        count+= 1
    if count==12:
        pass
    else:
         raise ValidationError("Invalid! Please enter a valid Aadhar Number.")


TYPE_CHOICES = (
    ('RED', 'Red'),
    ('Orange', 'Orange'),
    ('Green', 'Green'),
)

class Ticket(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    aadhar = models.IntegerField(validators=[twelvedigit])
    zone= models.CharField(max_length=10,choices=TYPE_CHOICES)
    passengers=models.IntegerField(validators=[crowd])
