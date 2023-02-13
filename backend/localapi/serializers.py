from rest_framework import serializers
from .models import RegisterUser,Addproduct,cartitems
class Customerserializers(serializers.ModelSerializer):
    class Meta:
        model=RegisterUser
        fields='__all__'
        
class Addserializers(serializers.ModelSerializer):
    class Meta:
        model=Addproduct
        fields='__all__'

class cartserializers(serializers.ModelSerializer):
    class Meta:
        model=cartitems
        fields='__all__'