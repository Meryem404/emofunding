from django.db import models
from datetime import datetime
# Create your models here.
class CreditCard(models.Model):
    name = models.CharField(max_length=30)
    number = models.IntegerField()
    security_code =  models.IntegerField()
    expiration_date = models.DateField()
    