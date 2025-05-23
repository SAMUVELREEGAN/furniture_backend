from rest_framework import serializers
from .models import *

class ContactUsMessageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactUsModel
        fields = '__all__'

class ContactSetiingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ContactSettingModel
        fields = '__all__'