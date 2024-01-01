from django.contrib import admin
from users.models import *

# Register your models here.
admin.site.register(NewUser)
admin.site.site_header = 'ShopCityMall'
