from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product, ProductOption
from products.serializers import ProductSerializer, ProductOptionSerializer


class ProductListAPIView(APIView):
    def get(self, request):
        qs = Product.objects.all()
        serializer = ProductSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def get(self, request, pk):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product)
        return Response(serializer.data)

    def put(self, request, pk):
        Product = self.get_object(pk)
        serializer = ProductSerializer(Product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        Product = self.get_object(pk)
        Product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductOptionListAPIView(APIView):

    def get(self, request):
        qs = ProductOption.objects.all()
        serializer = ProductOptionSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductOptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ProductOptionDetailAPIView(APIView):
    def get_objecjt(self, pk):
        return get_object_or_404(ProductOption, pk=pk)

    def get(self, request, pk):
        ProductOption = self.get_objecjt(pk)
        serializer = ProductOptionSerializer(ProductOption)
        return Response(serializer.data)

    def put(self, request, pk):
        ProductOption = self.get_object(pk)
        serializer = ProductOptionSerializer(ProductOption, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        ProductOption = self.get_objecjt(pk)
        ProductOption.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
