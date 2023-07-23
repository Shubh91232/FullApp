from django.db import models
# Create your models here.
class Tree(models.Model):
    Tree_id=models.CharField(max_length=255,primary_key=True)
    qrcode_id=models.CharField(max_length=255)
    TreeName=models.CharField(max_length=255)
    TreeDatile=models.TextField()