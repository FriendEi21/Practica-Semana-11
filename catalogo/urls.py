"""Rutas específicas de la aplicación catalogo."""

from django.urls import path
from .views import home, ProductoListView

# IA: Error NoReverseMatch al invocar rutas desde plantillas → Solución manual: Definir el parámetro 'name' en cada path() para permitir resolución inversa con {% url %} sin hardcodear rutas.
urlpatterns = [
    path('', home, name='home'),
    path('productos/', ProductoListView.as_view(), name='catalogo'),
]
