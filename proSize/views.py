from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ProductSize
from .serializers import ProductSizeSerializer

class ProductSizeListView(APIView):
    def get(self, request):
        sizes = ProductSize.objects.all()
        serializer = ProductSizeSerializer(sizes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
