from django.contrib import admin
from payments.models import *

# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display=["id","ref",'amount',"verified","date_created"]

admin.site.register(UserWallet)
admin.site.register(Payment, PaymentAdmin)
admin.site.site_header = 'ShopCityMall'
