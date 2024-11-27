from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializers import *
# Create your views here.

class Operation1(APIView):
    def post(self,request):
        serializer=CategorySerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def get(self,request):
        item=Category.objects.all()
        serializer=CategorySerializer(item,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

class Operation2(APIView):
    def get(self,request,pk):
        try:
            item=Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"Something went wrong"},status=status.HTTP_404_NOT_FOUND)
        
        serailizer=CategorySerializer(item)
        return Response(serailizer.data,status=status.HTTP_200_OK)
        
    def put(self,request,pk):
        try:
            item=Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"Not Found"},status=status.HTTP_400_BAD_REQUEST)
        
        serailizer=CategorySerializer(item,data=request.data)
        if(serailizer.is_valid()):
            serailizer.save()
            return Response({"Sucessfully Updated"},status=status.HTTP_200_OK)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        try:
            item=Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"Something went wrong"},status=status.HTTP_404_NOT_FOUND)
        
        serailizer=CategorySerializer(item,data=request.data,partial=True)
        if(serailizer.is_valid()):
            serailizer.save()
            return Response(serailizer.data,status=status.HTTP_200_OK)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,pk):
        try:
            item=Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response({"Something went wrong"},status=status.HTTP_404_NOT_FOUND)
        
        item.delete()
        return Response({"Delated"},status=status.HTTP_204_NO_CONTENT)
    
class Operations3(APIView):
    def post(self,request):
        temp=request.data.get('cat')
        try:
            item=Category.objects.get(id=temp)
        except Category.DoesNotExist:
            return Response({"Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serailizer=ProductSerializer(data=request.data)
        if(serailizer.is_valid()):
            serailizer.save()
            return Response(serailizer.data,status=status.HTTP_201_CREATED)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        item=Product.objects.all()
        serailizer=ProductSerializer(item,many=True)
        return Response(serailizer.data,status=status.HTTP_200_OK)

class Operation4(APIView):
    def get(self,request,pk):
        try:
            item=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"Not Found"},status=status.HTTP_404_NOT_FOUND)
        serailizer=ProductSerializer(item)
        return Response(serailizer.data,status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            item=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serailizer=ProductSerializer(item,data=request.data)
        if(serailizer.is_valid()):
            serailizer.save()
            return Response({"Updated"},status=status.HTTP_200_OK)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk):
        try:
            item=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response({"Not Found"},status=status.HTTP_404_NOT_FOUND)
        
        serailizer=ProductSerializer(item,data=request.data, partial=True)
        if(serailizer.is_valid()):
            serailizer.save()
            return Response(serailizer.data,status=status.HTTP_200_OK)
        return Response(serailizer.errors,status=status.HTTP_400_BAD_REQUEST)
        