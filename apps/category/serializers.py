from rest_framework import serializers

from apps.category.models import Category


class CategoryAPISerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = (
            "id", "title", "icon", "parent"
        )

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.child.exists():
            representation['child'] = CategoryAPISerializer(
                instance.child.all(), many=True
            ).data

        return representation
