# colorList/views.py

from rest_framework import generics
from .models import Color
from .serializers import ColorSerializer

class ColorListView(generics.ListAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
