from django.db import models

from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class Slider(models.Model):
    img = models.ImageField(upload_to='slider_images', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 1486px format.</h2>'))  # size must be ato ato pixel)

class Product(models.Model):
    CATEGORY = (
        ('UPCOMING PRODUCTS', 'UPCOMING PRODUCTS'),
        ('ORGANIC FOOD', 'ORGANIC FOOD'),
        ('MOST DEMANDABLE PRODUCTS', 'MOST DEMANDABLE PRODUCTS'),
        ('KHILMAR', 'KHILMAR'),
        ('JILBAB', 'JILBAB'),
        ('ABAYA/BORKA', 'ABAYA/BORKA'),
        ('LINEN', 'LINEN'),
        ('COTTON', 'COTTON'),
        ('CAPE', 'CAPE'),
        ('NIQAB', 'NIQAB'),
        ('HAND GLOVES & SOCKS', 'HAND GLOVES & SOCKS'),
        ('SUNNAH ITEM', 'SUNNAH ITEM'), 
    )
    name = models.CharField(max_length=50)
    description = models.TextField()
    pro_img = models.ImageField(upload_to='product_images', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 1486px format.</h2>'))  # size must be ato ato pixel)
    price = models.CharField(max_length=10)
    updated_price = models.CharField(max_length=10, blank=True, null=True)
    category = models.CharField(max_length=200, choices=CATEGORY, default=CATEGORY[0])

    def delete(self, using=None, keep_parents=False):
        self.pro_img.storage.delete(self.pro_img.path)
        super().delete()


class About(models.Model):
    text = models.TextField()
    abt_img = models.ImageField(upload_to='about_images', help_text=mark_safe('<h2 style="color: #008CBA;">Images size must be height: 1200px and width: 1486px format.</h2>'))  # size must be ato ato pixel)
