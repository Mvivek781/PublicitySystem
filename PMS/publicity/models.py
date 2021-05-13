from django.db import models

# Create your models here.
class Events(models.Model):
    name=models.CharField(max_length=60)
    desc = models.CharField(max_length=1000)
    photo = models.ImageField(default='',null=True,blank=True,upload_to='')

