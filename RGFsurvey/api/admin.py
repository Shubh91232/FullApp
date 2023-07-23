from django.contrib import admin
from .models import Tree

# Register your models here.
@admin.register(Tree)
class TreeAdmin(admin.ModelAdmin):
    list_display=['Tree_id','qrcode_id','TreeName','TreeDatile']
