from rest_framework import generics
from .models import WebLink
from .serializers import WebLinkSerializer

class WebLinkListView(generics.ListCreateAPIView):
    queryset = WebLink.objects.all()
    serializer_class = WebLinkSerializer
