from django.http import Http404
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Product
from .serializers import ProductSerializer, CategorySerializer

class LatestProductList(APIView): #viewset to get latest products to show in frontend
    def get(self,request, format= None):
        products = Product.objects.all()[0:4] #this shows number of items to be shown in latest products
        serializer =ProductSerializer(products, many=True)
        return Response(serializer.data)
        
class ProductDetail(APIView):
    def get_object(self,category_slug, product_slug):
        #check if product exists
        try:
            return Product.objects.filter(category__slug= category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            raise Http404
    def get(self,request, category_slug, product_slug, format=None):
        product= self.get_object(category_slug, product_slug)
        serializer= ProductSerializer(product)
        return Response(serializer.data)


class CategoryDetail(APIView):
    def get_object(self,category_slug):
        #check if product exists
        try:
            return Category.objects.get(slug=category_slug)
        except Product.DoesNotExist:
            raise Http404
    
    def get(self,request, category_slug, format=None):
        category= self.get_object(category_slug)
        serializer= CategorySerializer(category)
        return Response(serializer.data)


# Create your views here.
