# store/admin.py

from django.contrib import admin
from .models import Category, Collection, Product, Image, Variant

admin.site.register(Category)
admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Variant)
