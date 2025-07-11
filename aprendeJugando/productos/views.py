from django.shortcuts import render

# Create your views here.

def pedidos(request):
    return render(request, "productos/pedidos.html")

def pedido_detalle(request):
    return render(request, "productos/pedido_detalle.html")