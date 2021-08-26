from django.contrib import admin

from .models import Slider, Product, About
# Register your models here.
@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['img']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'updated_price', 'category']
    search_fields = ['name', 'price']
    list_filter = ['price']
    ordering = ['name']

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['text', 'abt_img']
