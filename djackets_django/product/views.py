from django.shortcuts import render
from rest_framework.serializers import Serializer

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

class LatestProductList(APIView): #viewset to get latest products to show in frontend
    def get(self,request, format= None):
        products = Product.objects.all()[0:4] #this shows number of items to be shown in latest products
        serializer =ProductSerializer(products, many=True)
        return Response(serializer.data)
        

# Create your views here.
