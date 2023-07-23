from django.shortcuts import render
from rest_framework.response import Response
from .models import Tree
from .serializers import TreeSerializer
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class TreeAPI(APIView):
    def get(self, request,pk=None,format=None):
        qrcode_id=pk
        if id is not None:
            tree = Tree.objects.get(qrcode_id=qrcode_id)
            serializer = TreeSerializer(tree)
            return Response(serializer.data)
        
        tree = Tree.objects.all()
        serializer = TreeSerializer(tree,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = TreeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        qrcode_id = pk
        tree=Tree.objects.get(qrcode_id=qrcode_id)
        serializer = TreeSerializer(tree,data=request.data)
        if serializer.is_valid():
            serializer.save()   
            return Response({'msg':'Completed Data Update'})
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk,format=None):
        qrcode_id=pk
        tree = Tree.objects.get(qrcode_id=qrcode_id)
        serializer = TreeSerializer(tree,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()   
            return Response({'msg':'Partial Data Updated'})
        return Response(serializer.errors)
    
    def delete(self,request,pk,format=None):
        qrcode_id=qrcode_id
        tree = Tree.objects.get(qrcode_id=qrcode_id)
        tree.delete()
        return Response({'msg':'Data Deleted'})

             