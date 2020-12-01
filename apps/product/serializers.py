from rest_framework import serializers
from apps.category.serializers import CategoryAPISerializer
from apps.product.models import Item


class ProductAPISerializer(serializers.ModelSerializer):
    category = CategoryAPISerializer(many=False, read_only=True)

    class Meta:
        model = Item
        fields = (
            'id', 'name', 'description', 'availability', 'price', 'quantity', 'author', 'category'
        )