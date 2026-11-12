"""Controladores de vista (FBV y CBV) bajo arquitectura MTV."""

from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


def home(request):
    """Vista Basada en Función (FBV) para la portada y resumen del sistema."""
    total_productos = Producto.objects.all().count()
    disponibles = Producto.objects.filter(disponible=True, stock__gt=0).count()

    contexto = {
        'titulo_sistema': 'sistema de gestión de inventario uncp',
        'total_productos': total_productos,
        'disponibles': disponibles,
    }
    return render(request, 'home.html', contexto)


class ProductoListView(ListView):
    """Vista Basada en Clases (CBV) para listar el catálogo de productos."""

    model = Producto
    template_name = 'catalogo.html'
    context_object_name = 'productos'

    # IA: ¿Por qué ListView no renderiza mis objetos personalizados y cómo inyectar datos extra al contexto? → Solución manual: Sobrescribir get_queryset() usando filter() y extender get_context_data() conservando la llamada a super().
    def get_queryset(self):
        """Obtiene los productos disponibles ordenados por fecha de registro."""
        return Producto.objects.filter(disponible=True).order_by('-fecha_registro')

    def get_context_data(self, **kwargs):
        """Inyecta metadatos adicionales al diccionario de contexto del template."""
        context = super().get_context_data(**kwargs)
        context['titulo_pagina'] = 'catálogo general de productos'
        return context
