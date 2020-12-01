from django.urls import path, include
from rest_framework import routers

from apps.product.views import (
    CustomerProductViewSet, ViewerProductAPIView
)

router = routers.SimpleRouter()
router.register('customer_products', CustomerProductViewSet, basename='customer_products')

urlpatterns = [
    path('viewer_products/', ViewerProductAPIView.as_view()),
]
urlpatterns += router.urls