from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Vendor)
admin.site.register(models.Unit)


class CustomerAdmin(admin.ModelAdmin):
    search_fields=['customer_name','customer_mobile']
    list_display=['customer_name','customer_mobile','customer_address']

admin.site.register(models.Customer,CustomerAdmin)



class ProductAdmin(admin.ModelAdmin):
    search_fields=['title','unit__title']
    list_display=['title','unit']
admin.site.register(models.Product,ProductAdmin)


class PurchaseAdmin(admin.ModelAdmin):
    search_fields=['product__title']
    list_display=['id','vendor','product','qty','price','total_amt','vendor','pur_date']
admin.site.register(models.Purchase,PurchaseAdmin)


class SaleAdmin(admin.ModelAdmin):
    search_fields=['product__title']
    list_display=['id','customer','product','qty','price','total_amt','sale_date']
admin.site.register(models.Sale,SaleAdmin)


class InventoryAdmin(admin.ModelAdmin):
    search_fields=['product__title','product__unit__title']
    list_display=['product','vendor','pur_qty','sale_qty','total_bal_qty','product_unit','pur_date','sale_date']
admin.site.register(models.Inventory,InventoryAdmin)


