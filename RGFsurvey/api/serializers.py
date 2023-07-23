from rest_framework import serializers
from .models import Tree

class TreeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tree
        fields=['Tree_id','qrcode_id','TreeName','TreeDatile']
