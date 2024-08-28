# store/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name='list_products'),
    path('variants/', views.list_variants, name='list_variants'),
    path('collections/', views.list_collections, name='list_collections'),
    path('collections/<int:collection_id>/products/', views.list_products_in_collection, name='list_products_in_collection'),
    path('collections/<int:collection_id>/variants/', views.list_variants_in_collection, name='list_variants_in_collection'),
    path('categories/<int:category_id>/variants/', views.list_variants_in_category, name='list_variants_in_category'),
]