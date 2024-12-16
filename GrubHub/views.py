from django.shortcuts import render
from django.http import HttpResponse,Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

def home(request):
    return HttpResponse("helooo")

class CategoryView(APIView):
    def get_object(pk):
        try:
            Category.objects.get(pk=pk)
        except :
            raise Http404
        
    def get(self,request):
        categories = Category.objects.all()
        seriailzer = CategorySerializer(categories,many=True)
        return Response(seriailzer.data)
    
    def get(self,request,pk):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def post(self,request):
        data = request.data
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class RestaurantListView(generics.ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    
class RestaurantView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
