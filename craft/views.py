from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response



class Craft(ListAPIView):
    queryset = Craft.objects.all()
    serializer_class = CraftSizeSerializer
