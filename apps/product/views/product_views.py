from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from apps.product.models.product import Product
from apps.product.serializers.product_serializer import ProductSerializer, ProductUpdateSerializer


class ProductViewsets(viewsets.GenericViewSet):
    queryset = Product.objects.filter(state=True)

    def get_serializer_class(self):
        if self.action == "update":
            return ProductUpdateSerializer
        return ProductSerializer
    
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.get_serializer(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        query = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(query, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(product, data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
