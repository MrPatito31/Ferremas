from django.shortcuts import render

def catalogo(request):
    return render(request, 'core/catalogo.html')

def carro(request):
    return render(request, 'core/carro.html')

def login(request):
    return render(request, 'core/login.html')