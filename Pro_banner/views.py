from django.shortcuts import render
from .serializers import *
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

    


class ProductBanner(UpdateAPIView):
    queryset = Pro_Banner.objects.all()
    serializer_class = Pro_BannerSerializers

class LatestProductBanner(APIView):
    def get(self, request):
        latest_banner = Pro_Banner.objects.latest('updated_at')
        serializer = Pro_BannerSerializers(latest_banner)
        return Response(serializer.data)