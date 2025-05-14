from django.urls import path
from .views import *

urlpatterns = [
     path('latest/', LatestLogoView.as_view(), name='latest-logo'),
     path('logo-images/<int:pk>/',LogoCreate.as_view(),name='logo-images'),
     path('productbanner/', LatestProductBanner.as_view(), name='latest-banner'),
     path('banner-images/<int:pk>/',ProductBanner.as_view(),name='banner-images'),
   ]
