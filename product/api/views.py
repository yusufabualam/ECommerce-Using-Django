from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from product.models import Product
from rest_framework.decorators import api_view

# Show -------------------------------------------------------------
@api_view(['GET'])
def getbyid(request,id):
    productdata=Product.objects.filter(id=id)
    if(len(productdata)>0):
        return Response(data={'data':ProductSerializer(productdata[0]).data},status=200)
    return Response({'msg':'product not found'},status=200)
# Delete ------------------------------------------------------------------
@api_view(['DELETE'])
def deletebyid(request,id):
    productdata=Product.objects.filter(id=id)
    if(len(productdata)>0):
        productdata.delete()
        return Response(data={'msg':'deleted'})
    return Response({'msg':'Product not found'})
# List ---------------------------------------------------------------------
@api_view(['GET'])
def getall(request):
    products=Product.get_all_products()
    selizeddata=[]
    for product in products:
        selizeddata.append(ProductSerializer(product).data)

    return Response({"msg":"done","data":selizeddata})  
# Insert ----------------------------------------------------------------------
@api_view(['POST'])
def add(request):
    product=ProductSerializer(data=request.data)
    if(product.is_valid()):
        product.save()
        return  Response({'msg':'Product added'})
    return Response(product.errors,status=400)
# Update ----------------------------------------------------------------------
@api_view(['GET','PUT'])
def updatebyid(request,id):
    productdata = Product.objects.filter(id=id).first()

    if(productdata):
        serlizeddata=ProductSerializer(instance=productdata,data=request.data)
        if serlizeddata.is_valid():
            serlizeddata.save()
            return Response(data=serlizeddata.data,status=200)
    return Response(serlizeddata.errors,status=400)