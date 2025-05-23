from rest_framework import serializers
from .models import *

class CraftSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Craft
        fields = '__all__'

