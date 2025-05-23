from rest_framework import serializers
from .models import *

class InfoSerializers(serializers.ModelSerializer):
    class Meta:
        model =Info
        fields = '__all__'