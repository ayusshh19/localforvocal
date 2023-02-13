from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Customerserializers,Addserializers,cartserializers
from rest_framework import status
from .models import RegisterUser,Addproduct,cartitems
# Create your views here.
@api_view(['GET','POST'])
def registeruser(request):
    if request.method=='GET':
        return Response({'msg':'Please register yourself'},status=status.HTTP_200_OK)
    
    if request.method=='POST':
        serializers=Customerserializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'msg':'You have registered successfully!!'},status=status.HTTP_200_OK)
        return Response({'msg':serializers.errors},status=status.HTTP_403_FORBIDDEN)
    
@api_view(['GET','POST'])        
def loginuser(request):
    if request.method=='GET':
        return Response({'msg':'Welcome user login to proceed!!'},status=status.HTTP_200_OK)
    
    if request.method=='POST':
        username=request.data['username']
        password=request.data['password']
        try:
          userexist=RegisterUser.objects.filter(username=username,password=password)
          if userexist.exists():
              request.session['username']=username
              RegisterUser.save()
              return Response({'msg':'successfully logged in!!'},status=status.HTTP_200_OK)
          return Response({'msg':'Pls register yourself before login!!'},status=status.HTTP_404_NOT_FOUND)
        except :
          return Response({'msg':'Something went wrong!!'},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET','POST'])
def Sellerproductlist(request,*args, **kwargs):
    if request.method=='GET':
        username=kwargs['username']
        try:
          userobj=RegisterUser.objects.get(username=username)
          productdetails=Addproduct.objects.filter(produser=userobj)
          serializers=Addserializers(productdetails,many=True)
          return Response({'msg':serializers.data},status=status.HTTP_200_OK)
        except:
          return Response({'msg':'something went wrong!!!'},status=status.HTTP_200_OK)
    
@api_view(['GET'])
def orderlist(request,*args, **kwargs):
    if request.method=='GET':
        username=kwargs['username']
        try:
          userobj=RegisterUser.objects.get(username=username)
          cartproducts=cartitems.objects.filter(userid=userobj)
          getallproducts=Addproduct.objects.all()
          serializers=cartserializers(cartproducts,many=True)
          productserializer=Addserializers(getallproducts,many=True)
          print(serializers.data)
          return Response({'orderlist':serializers.data,'productlist':productserializer.data},status=status.HTTP_200_OK)
        except:
          return Response({'msg':'something went wrong!!!'},status=status.HTTP_200_OK)