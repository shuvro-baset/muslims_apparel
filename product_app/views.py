from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# import paginator classes
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger



# todo: render home page and showing few types of product and also slider images from backend.
def home(request):
    # fetch all slider images from slide model
    slider_ins = Slider.objects.all().order_by('id')
    # fetch all products instances from product model
    product_ins = Product.objects.all().order_by('-id')
    upcoming_prdct_ins = Product.objects.filter(category='UPCOMING PRODUCTS').order_by('-id')[:8]
    organic_food_ins = Product.objects.filter(category='ORGANIC FOOD').order_by('-id')[:8]
    most_demandable_prdct_ins = Product.objects.filter(category='MOST DEMANDABLE PRODUCTS').order_by('-id')[:8]
    sunnar_item_ins = Product.objects.filter(category='SUNNAH ITEM').order_by('-id')[:8]
    niqab_item_ins = Product.objects.filter(category='NIQAB').order_by('-id')[:8]
    about_ins = About.objects.all().first()
    context = {
        'products': product_ins,
        'sliders': slider_ins,
        'upcoming_prdct_ins': upcoming_prdct_ins,
        'organic_food_ins': organic_food_ins,
        'most_demandable_prdct_ins': most_demandable_prdct_ins,
        'sunnar_item_ins': sunnar_item_ins,
        'niqab_item_ins': niqab_item_ins,
        'about_ins': about_ins
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

        paginator = Paginator(context['products'], 2) # Show 25 contacts per page.
        # print(paginator)
        page_number = self.request.GET.get("page", 1)
        print("page Number: ",page_number)
        page_obj = paginator.get_page(page_number)

        context['page_obj'] = page_obj

        return context

# todo: single product view
class SinglepProductView(TemplateView):
    template_name = 'product-single.html'

    def get_context_data(self, product_id, **kwargs):
        context = super().get_context_data(**kwargs)
        # filtering product using product id
        context['product'] = Product.objects.filter(id=product_id).first()
        return context


def privacy(request):
    return render(request, 'privacy.html')