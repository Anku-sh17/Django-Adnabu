# store/models.py

from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey('self', related_name='subcategories', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Collection(models.Model):
    title = models.CharField(max_length=255)
    published = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField(Category, related_name='products')
    collections = models.ManyToManyField(Collection, related_name='products', blank=True)

    def __str__(self):
        return self.title

class Image(models.Model):
    source = models.ImageField(upload_to='product_images/')
    alt_text = models.CharField(max_length=255, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.alt_text or self.source.name

class Variant(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    available_for_sale = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    image = models.ForeignKey(Image, related_name='variants', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product.title} - {self.title}"
