from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializer import ProductSerializer
# Create your views here.

@api_view(['GET','POST'])
def product_list(request):
    if request.method=='GET':
        cityFilter=request.GET.get('city','')
        rentFilter=request.GET.get('rent',)

        pageCount=request.GET.get('pageCount',1)
        productsPerPage=request.GET.get('itemsPerPage',50)

        sortType=request.GET.get('sortType','asc')
        sortParams=request.GET.get('sortObject','')

        #Multiple-Ordering
        order_by_list=sortParams.split(',')

        if not cityFilter and rentFilter:
            products=Product.objects.all()
        else:
            #Implementing filtering and ordering functionality
            products.Product.objects.filter(city=cityFilter).order_by(order_by_list)
            for product in products.Product.objects:
                if product.rent>rentFilter:
                    product.remove()

        #pagination support for smooth loading
        productToSkip=(pageCount-1)*productsPerPage
        products=products[productToSkip:productToSkip+productsPerPage]

        serializer=ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
#pk-> primary key to get unique apartment as pathParam 
@api_view(['PUT','DELETE'])
def product_detail(request,pk):
    try:
        product=Product.objects.get(pk=pk)
    except product.DoesNotExists:
        return Response({'error':'Product not found'},status=status.HTTP_404_NOT_FOUND)
    

    if request.method=="PUT":
        serializer=ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method=="DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

