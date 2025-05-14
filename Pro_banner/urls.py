from django.urls import path
from .views import *

urlpatterns = [
     path('productbanner/', LatestProductBanner.as_view(), name='latest_banner'),
     path('banner-images/<int:pk>/',ProductBanner.as_view(),name='banner-images'),
   ]
