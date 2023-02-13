from django.contrib import admin
from .models import RegisterUser,Addproduct,cartitems

# Register your models here.
@admin.register(RegisterUser)
class RegisterUserAdmin(admin.ModelAdmin):
    list_display=[f.name for f in RegisterUser._meta.fields]

    
# Register your models here.
@admin.register(Addproduct)
class Addproductadmin(admin.ModelAdmin):
    list_display=[f.name for f in Addproduct._meta.fields]

# Register your models here.
@admin.register(cartitems)
class cartitemadmin(admin.ModelAdmin):
    list_display=[f.name for f in cartitems._meta.fields]