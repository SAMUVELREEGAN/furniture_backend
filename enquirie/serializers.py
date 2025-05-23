from rest_framework import serializers
from .models import enquiriesModel

class enquiriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = enquiriesModel
        fields = '__all__'