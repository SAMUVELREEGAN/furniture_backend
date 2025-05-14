from rest_framework import serializers
from .models import *

class Pro_BannerSerializers(serializers.ModelSerializer):
    class Meta:
        model =Pro_Banner
        fields = '__all__'