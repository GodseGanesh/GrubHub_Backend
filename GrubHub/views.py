from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView

def home(request):
    return HttpResponse("helooo")
