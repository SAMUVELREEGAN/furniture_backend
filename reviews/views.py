from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView
from .models import Review
from .serializers import ReviewSerializer

class ReviewListView(ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
