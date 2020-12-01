from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from apps.product.models import Item
from apps.product.permissions import IsCustomer
from apps.product.serializers import ProductAPISerializer


class CustomerProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductAPISerializer
    queryset = Item.objects.all()
    permission_classes = (IsAuthenticated, IsCustomer, )

    def get_queryset(self):
        return Item.objects.filter(
            author=self.request.user
        )


class ViewerProductAPIView(ListAPIView):
    queryset = Item.objects.all()
    permission_classes = (IsAuthenticated, )
    serializer_class = ProductAPISerializer




