from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Cart, Order
from apps.product.models import Item


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'addresses', 'carts')
        write_only_fields = ('password', )

    def restore_object(self, attrs, instance=None):
        user = super(AccountSerializer, self).restore_object(attrs, instance)
        user.set_password(attrs['password'])
        return user


class CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ('url', 'items', )


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('url', 'items', 'cart')


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Item
        fields = (
            'name', 'description', 'availability', 'price', 'date_created', 'category', 'author',
        )


class AuditSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url', 'username', 'email', 'password', 'addresses', 'carts'
        )
        write_only_fields = ('password', )
