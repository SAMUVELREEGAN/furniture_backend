from rest_framework.generics import ListAPIView, CreateAPIView
from .models import Info
from .serializers import InfoSerializers

class InfoListView(ListAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers

class InfoCreateView(CreateAPIView):
    queryset = Info.objects.all()
    serializer_class = InfoSerializers
