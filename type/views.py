# type/views.py

from rest_framework import generics
from .models import Type
from .serializers import TypeSerializer

class TypeListView(generics.ListAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer
