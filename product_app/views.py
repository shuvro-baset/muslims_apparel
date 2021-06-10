from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'home.html'


def home(request):
    slider_ins = Slider.objects.all().order_by('-id')
    print(slider_ins)
    product_ins = Product.objects.all().order_by('-id')
    context = {
        'products': product_ins,
        'sliders': slider_ins,
    }
    return render(request, 'home.html', context)

class ProductView(TemplateView):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.request.GET.get('category')
        print(category)
        context['products'] = Product.objects.filter(category=category).all()
        print(context['products'])
        return context
