from django.shortcuts import render
from shop.models import Product  # <-- Xatoni o'ldirgan eng muhim qator! Omborxonani uladik.
from django.shortcuts import get_object_or_404

def bosh_sahifa(request):
    # Bosh sahifa uchun 4 tadan tovar chaqiramiz
    best_sellers = Product.objects.filter(is_bestseller=True).order_by('-id')[:4]
    new_arrivals = Product.objects.filter(is_new=True).order_by('-id')[:4]

    context = {
        'best_sellers': best_sellers,
        'new_arrivals': new_arrivals
    }
    return render(request, 'index.html', context)


def katalog(request):
    # Katalog uchun bazadagi BARCHA tovarlarni olamiz
    barcha_mahsulotlar = Product.objects.all().order_by('-id')

    context = {
        'products': barcha_mahsulotlar
    }
    return render(request, 'katalog.html', context)


def biz_haqimizda(request):
    return render(request, 'biz_haqimizda.html')


def savatcha(request):
    return render(request, 'savatcha.html')


def profil(request):
    return render(request, 'profil.html')



def mahsulot_batafsil(request, pk):
    # Bazadan bittagina tovarni ID orqali topib olamiz
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'mahsulot_batafsil.html', context)