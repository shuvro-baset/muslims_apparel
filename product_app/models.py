from django.db import models

# Create your models here.
class Slider(models.Model):
    img = models.ImageField(upload_to='slider_images')

class Product(models.Model):
    CATEGORY = (
        ('NEW ARRIVALS', 'NEW ARRIVALS'),
        ('ORGANIC FOOD', 'ORGANIC FOOD'),
        ('BEST SELLING PRODUCTS', 'BEST SELLING PRODUCTS'),
        ('TOP RATED PRODUCTS', 'TOP RATED PRODUCTS'),
        ('KHILMAR', 'KHILMAR'),
        ('JILBAB', 'JILBAB'),
        ('ABAYA/BORKA', 'ABAYA/BORKA'),
        ('LINEN', 'LINEN'),
        ('COTTON', 'COTTON'),
        ('CAPE', 'CAPE'),
        ('NIQAB', 'NIQAB'),
        ('HAND GLOVES & SOCKS', 'HAND GLOVES & SOCKS'),
        ('SUNNAH ITEM', 'SUNNAH ITEM'),
        ('ORGANIC FOOD', 'ORGANIC FOOD'),
    )
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    pro_img = models.ImageField(upload_to='product_images')
    price = models.CharField(max_length=10)
    updated_price = models.CharField(max_length=10, blank=True, null=True)
    category = models.CharField(max_length=200, choices=CATEGORY, default=CATEGORY[0])