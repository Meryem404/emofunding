from django.db import models

# Create your models here.
class creator(models.Model):
    bank_account = models.IntegerField()
    paypal_url = models.URLField(max_length = 200)
