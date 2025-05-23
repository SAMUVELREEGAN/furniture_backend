from django.urls import path
from .views import CarouselImageList

urlpatterns = [
    path('', CarouselImageList.as_view(), name='carousel-images'),
]
