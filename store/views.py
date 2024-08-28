# store/views.py

from django.http import JsonResponse
from .models import Product, Variant, Collection, Category

def list_products(request):
    products = Product.objects.all()
    products_data = [{
        "title": product.title,
        "description": product.description,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
        "images": [image.source.url for image in product.images.all()]
    } for product in products]
    
    return JsonResponse(products_data, safe=False)

def list_variants(request):
    variants = Variant.objects.all()
    variants_data = [{
        "title": f"{variant.product.title} - {variant.title}",
        "created_at": variant.created_at,
        "updated_at": variant.updated_at,
        "available_for_sale": variant.available_for_sale,
        "price": variant.price,
        "image": variant.image.source.url,
    } for variant in variants]

    return JsonResponse(variants_data, safe=False)

def list_collections(request):
    collections = Collection.objects.all()
    collections_data = [{
        "title": collection.title,
        "published": collection.published,
        "updated_at": collection.updated_at,
    } for collection in collections]

    return JsonResponse(collections_data, safe=False)

def list_products_in_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    products = collection.products.all()
    products_data = [{
        "title": product.title,
        "description": product.description,
        "created_at": product.created_at,
        "updated_at": product.updated_at,
        "images": [image.source.url for image in product.images.all()]
    } for product in products]

    return JsonResponse(products_data, safe=False)

def list_variants_in_collection(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    variants = Variant.objects.filter(product__collections=collection)
    variants_data = [{
        "title": f"{variant.product.title} - {variant.title}",
        "created_at": variant.created_at,
        "updated_at": variant.updated_at,
        "available_for_sale": variant.available_for_sale,
        "price": variant.price,
        "image": variant.image.source.url,
    } for variant in variants]

    return JsonResponse(variants_data, safe=False)

def list_variants_in_category(request, category_id):
    category = Category.objects.get(id=category_id)
    variants = Variant.objects.filter(product__categories=category)
    variants_data = [{
        "title": f"{variant.product.title} - {variant.title}",
        "created_at": variant.created_at,
        "updated_at": variant.updated_at,
        "available_for_sale": variant.available_for_sale,
        "price": variant.price,
        "image": variant.image.source.url,
    } for variant in variants]

    return JsonResponse(variants_data, safe=False)

