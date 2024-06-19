from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .models import *
from django.contrib.auth.views import logout_then_login
from .forms import *
from django.urls import reverse
import paypalrestsdk
from .models import Producto, Venta, DetalleVenta
from .paypal import paypalrestsdk

def registro_login_view(request):
    registro_form = RegistroForm()
    login_form = LoginForm()
    
    if request.method == "POST":
        if 'register' in request.POST:
            registro_form = RegistroForm(request.POST)
            if registro_form.is_valid():
                user = registro_form.save()
                login(request, user)
                messages.success(request, "Registro exitoso.")
                return redirect('inicio')
        elif 'login' in request.POST:
            login_form = LoginForm(data=request.POST)
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"Bienvenido {username}!")
                    return redirect('inicio')
                else:
                    messages.error(request, "Credenciales incorrectas.")
    
    return render(request, "core/login.html", {"registro_form": registro_form, "login_form": login_form})

def inicio_view(request):
    return render(request, "catalogo.html")

def catalogo(request):
    producto = Producto.objects.all()
    context = {'producto':producto}
    carro = request.session.get("carro", [])
    context["carro"] = carro
    return render(request, 'core/catalogo.html', context)

def logout(request):
    return logout_then_login(request, login_url="registro_login")

def administrador(request):
    return render(request, 'core/administrador.html')

def pago_view(request):
    context = {}
    carro = request.session.get("carro", [])
    context["carro"] = carro
    return render(request, 'core/pago.html', context)

def bodega(request):
    return render(request, 'core/bodega.html')

def addtocar(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            item[5] += 1
            item[6] = item[4] * item[5]
            break
    else:
        carro.append([codigo, producto.nombre, producto.descripcion, producto.imagen, producto.precio, 1, producto.precio])
    request.session["carro"] = carro
    return redirect(to="catalogo")

def dropitem(request, codigo):
    carro = request.session.get("carro", [])
    for item in carro:
        if item[0] == codigo:
            if item[5] >= 1:
                item[5] -= 1
                item[6] = item[4] * item[5]
                break
            else:
                carro.remove(item)
    request.session["carro"] = carro
    return redirect(to="catalogo")

def limpiar(request):
    request.session.flush()
    return redirect(to="catalogo")

def pago(request):
    carro = request.session.get("carro", [])
    total = sum(item[6] for item in carro)

    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"},
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute')),
            "cancel_url": request.build_absolute_uri(reverse('catalogo'))},
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": item[1],
                    "sku": item[0],
                    "price": str(item[4]),
                    "currency": "USD",
                    "quantity": item[5]} for item in carro]},
            "amount": {
                "total": str(total),
                "currency": "USD"},
            "description": "Compra en la tienda"}]})

    if payment.create():
        for link in payment.links:
            if link.rel == "approval_url":
                approval_url = str(link.href)
                return redirect(approval_url)
    else:
        print(payment.error)
        return redirect('catalogo')

def execute(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return comprar(request)
    else:
        print(payment.error)
        return redirect('catalogo')

def comprar(request):
    if not request.user.is_authenticated:
        return redirect(to="login")

    carro = request.session.get("carro", [])
    total = sum(item[6] for item in carro)
    venta = Venta(cliente=request.user, total=total)
    venta.save()

    for item in carro:
        producto = Producto.objects.get(codigo=item[0])
        detalle = DetalleVenta(
            producto=producto,
            precio=item[4],
            cantidad=item[5],
            venta=venta
        )
        producto.stock -= item[5]
        detalle.save()
        producto.save()

    request.session["carro"] = []
    return redirect(to="catalogo")

def historial(request):
    if not request.user.is_authenticated:
        return redirect(to="login")
    ventas = Venta.objects.filter(cliente=request.user)
    context = {"ventas":ventas}
    return render(request, 'core/catalogo.html', context)