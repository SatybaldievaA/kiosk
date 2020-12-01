from django.shortcuts import render

from rest_framework.generics import ListAPIView

from apps.category.models import Category
from .serializers import CategoryAPISerializer

class CategoryApiView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryAPISerializer