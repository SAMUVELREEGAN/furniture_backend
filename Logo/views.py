from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class LogoCreate(UpdateAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializers

# class LogoList(ListAPIView):
#     queryset = Logo.objects.all()
#     serializer_class = LogoSerializers

class LatestLogoView(APIView):
    def get(self, request):
        latest_logo = Logo.objects.latest('updated_at')
        serializer = LogoSerializers(latest_logo)
        return Response(serializer.data)
    


class ProductBanner(UpdateAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializers

class LatestProductBanner(APIView):
    def get(self, request):
        latest_logo = Logo.objects.latest('updated_at')
        serializer = LogoSerializers(latest_logo)
        return Response(serializer.data)