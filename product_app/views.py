from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *

# todo: render home page and showing few types of product and also slider images from backend.
def home(request):
    # fetch all slider images from slide model
    slider_ins = Slider.objects.all().order_by('-id')
    # fetch all products instances from product model
    product_ins = Product.objects.all().order_by('-id')
    new_arrival_ins = Product.objects.filter(category='NEW ARRIVALS').order_by('-id')[:8]
    organic_food_ins = Product.objects.filter(category='ORGANIC FOOD').order_by('-id')[:8]
    best_selling_product_ins = Product.objects.filter(category='BEST SELLING PRODUCTS').order_by('-id')[:8]
    top_rated_products_ins = Product.objects.filter(category='TOP RATED PRODUCTS').order_by('-id')[:8]
    print(new_arrival_ins)

    context = {
        'products': product_ins,
        'sliders': slider_ins,
        'new_arrivals': new_arrival_ins,
        'organic_food_ins': organic_food_ins,
        'best_selling_product_ins': best_selling_product_ins,
        'top_rated_products_ins': top_rated_products_ins,
    }
    return render(request, 'home.html', context)

# todo: all product view
class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # taking category from request
        category = self.request.GET.get('category')
        # taking all products based on category using filter method
        context['products'] = Product.objects.filter(category=category).all()
        # appending another value into context data
        context['category'] = category
        return context

# todo: single product view
class SinglepProductView(TemplateView):
    template_name = 'product-single.html'

    def get_context_data(self, product_id, **kwargs):
        context = super().get_context_data(**kwargs)
        # filtering product using product id
        context['product'] = Product.objects.filter(id=product_id).first()
        return context