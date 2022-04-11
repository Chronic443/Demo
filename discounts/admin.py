from django.contrib import admin
from .models import Discount, DiscountCode

DiscountModels = [Discount, DiscountCode]
admin.site.register(DiscountModels)
