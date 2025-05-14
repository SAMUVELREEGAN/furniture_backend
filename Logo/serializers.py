from rest_framework import serializers
from .models import *

class LogoSerializers(serializers.ModelSerializer):
    class Meta:
        model =Logo
        fields = '__all__'