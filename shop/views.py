from itertools import product
from django.shortcuts import render
from store.models import Product


#Функция home выводит "Homepage", т.е. эта первая кастомная страница после создания проекат джанго
def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)