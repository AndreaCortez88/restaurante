from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    allBebidas = Bebidas.objects.all()
    allPostres = Postres.objects.all()
    allExtras = Extras.objects.all()
    return render(request, 'index.html', {'allBebidas':allBebidas,
                                          'allPostres':allPostres,
                                          'allExtras':allExtras})

def Contact(request):
    return render(request, 'contact.html')


def About(request):
    return render(request, 'about.html')

def Carrito(request):
    return render(request, 'carrito.html')