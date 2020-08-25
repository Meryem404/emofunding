from django.db import models 
from creator.models import creator
from embed_video.fields import EmbedVideoField
#Create your models here.
class Projet(models.Model):
    creator = models.ForeignKey(creator, on_delete = models.DO_NOTHING)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    video = EmbedVideoField()
    amount = models.IntegerField()
    time = models.IntegerField()
    image_main = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)

