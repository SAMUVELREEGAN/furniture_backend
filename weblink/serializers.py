from rest_framework import serializers
from .models import WebLink

class WebLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebLink
        fields = ['id', 'link_name']
