# from django.shortcuts import render

# from django.http import JsonResponse
# from .models import Category, Product

# def product_list(request):
#     products = Product.objects.all()
#     return JsonResponse([p.to_json() for p in products], safe=False)

# def product_detail(request, id):
#     try:
#         product = Product.objects.get(id=id)
#         return JsonResponse(product.to_json())
#     except Product.DoesNotExist:
#         return JsonResponse({'error': 'Product not found'}, status=404)

# def category_list(request):
#     categories = Category.objects.all()
#     return JsonResponse([c.to_json() for c in categories], safe=False)

# def category_detail(request, id):
#     try:
#         category = Category.objects.get(id=id)
#         return JsonResponse(category.to_json())
#     except Category.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status=404)

# def category_products(request, id):
#     try:
#         category = Category.objects.get(id=id)
#         products = Product.objects.filter(category=category)
#         return JsonResponse([p.to_json() for p in products], safe=False)
#     except Category.DoesNotExist:
#         return JsonResponse({'error': 'Category not found'}, status=404)

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api.models import Category, Product
from api.serializers import CategorySerializer, ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # Это для запроса /api/categories/<id>/products/
    @action(detail=True, methods=['get'])
    def products(self, request, pk=None):
        category = self.get_object()
        products = Product.objects.filter(category=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer