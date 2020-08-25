from django.db import models
from creditCard.models import CreditCard
# Create your models here.
class investor(models.Model):
    creditCard = models.ForeignKey(CreditCard, on_delete = models.DO_NOTHING)
    amount = models.IntegerField()

