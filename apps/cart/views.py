from django.contrib.auth.models import User

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .serializers import AccountSerializer, CartSerializer, ProductSerializer, OrderSerializer, AuditSerializer
from .models import Cart, Order
from ..product.models import Item


class AccountViewSet(viewsets.ModelViewSet):
    model = User
    serializer_class = AccountSerializer
    permission_classes = ()

    def get_queryset(self, ):
        user = self.request.user
        return User.objects.filter(username=user.username)

    def post_save(self, obj, created=False):
        if created:
            cart = Cart(user=obj)
            cart.save()


class CartViewSet(viewsets.ModelViewSet):
    model = Cart
    serializer_class = CartSerializer

    def get_queryset(self, ):
        return Cart.objects.filter(user=self.request.user)

    """
    creating product and adding it to the cart of customer
    """

    @action()
    def add(self, request, pk):
        return Response({"success": True})

    def pre_save(self, obj):
        obj.user = self.request.user


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(viewsets.ModelViewSet):
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self, ):
        return Order.objects.filter(user=self.request.user)

    def pre_save(self, obj):
        obj.user = self.request.user


class DetailedAccountViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = AuditSerializer
    permission_classes = (IsAdminUser, )
