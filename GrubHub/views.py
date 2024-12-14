from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Category
from .serializers import CategorySerializer

def home(request):
    return HttpResponse("helooo")

class CategoryView(APIView):
    def get(self,request):
        categories = Category.objects.all()
        seriailzer = CategorySerializer(categories,many=True)
        return Response(seriailzer.data)
    def post(self,request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)