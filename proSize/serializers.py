from rest_framework import serializers
from .models import ProductSize

class ProductSizeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='category.categorie')

    class Meta:
        model = ProductSize
        fields = ['id', 'name']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        sizes = [s.strip() for s in instance.sizes.split(',') if s.strip()]
        for i, size in enumerate(sizes):
            rep[f"size{i+1}"] = size
        return rep
