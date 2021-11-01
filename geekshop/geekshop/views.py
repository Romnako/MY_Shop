from django.shortcuts import render
from mainapp.models import Product
from basketapp.models import Basket

def main(request):
    title = 'Магазин'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    products = Product.objects.all()[1:4]

    context = {
        'title': title,
        'products': products,
        'basket': basket,
        'basket_count': basket
    }
    return render(request, 'geekshop/index.html', context=context)

def contacts(request):
    title = 'Контакты'
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'basket': basket,

    }
    return render(request, 'geekshop/contact.html', context=context)