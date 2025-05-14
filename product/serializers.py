from rest_framework import serializers
from .models import Product, ProductImage

# Serializer for product images
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']

# Main Product serializer with names instead of IDs
class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    category = serializers.StringRelatedField()
    color = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    size = serializers.StringRelatedField()
    link_name = serializers.StringRelatedField()

    class Meta:
        model = Product
        fields = [
            'id', 'pro_name', 'description', 'star', 'price',
            'category', 'color', 'type', 'size', 'link_name',
            'images'
        ]
