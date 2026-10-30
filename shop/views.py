from django.shortcuts import render
from shop.models import Product  # Yangi omborxonamizdan tovarlarni chaqirdik!

def bosh_sahifa(request):
    # Bazadan TOP va YANGI tovarlarni ajratib olib, 4 tadan jo'natamiz
    best_sellers = Product.objects.filter(is_bestseller=True).order_by('-id')[:4]
    new_arrivals = Product.objects.filter(is_new=True).order_by('-id')[:4]

    context = {
        'best_sellers': best_sellers,
        'new_arrivals': new_arrivals
    }
    return render(request, 'index.html', context)

def katalog(request):
    return render(request, 'katalog.html')

def biz_haqimizda(request):
    return render(request, 'biz_haqimizda.html')

def savatcha(request):
    return render(request, 'savatcha.html')

def profil(request):
    return render(request, 'profil.html')