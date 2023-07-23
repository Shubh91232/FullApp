from django.db import models

# Create your models here.
class TreeDigitalLibrary(models.Model):
    Tree_id=models.IntegerField(primary_key=True)
    qrcode_id=models.CharField(max_length=255)
    ComanName=models.CharField(max_length=255)
    BotanicalName=models.IntegerField()
    
