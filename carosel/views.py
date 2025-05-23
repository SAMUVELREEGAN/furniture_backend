from rest_framework.views import APIView
from rest_framework.response import Response
from .models import CarouselImage
from .serializers import CarouselImageSerializer

class CarouselImageList(APIView):
    def get(self, request):
        images = CarouselImage.objects.all()
        serializer = CarouselImageSerializer(images, many=True, context={'request': request})
        return Response(serializer.data)
