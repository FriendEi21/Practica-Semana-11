"""Modelos de datos gestionados por el ORM de Django."""

from django.db import models


class Producto(models.Model):
    """Representa un producto dentro del inventario en SQLite."""

    nombre = models.CharField(max_length=120)
    categoria = models.CharField(max_length=60)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    disponible = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    # Declaración explícita del Manager para análisis estático (Pylint)
    objects = models.Manager()

    # IA: Lógica de negocio acoplada en las vistas → Solución manual: Delegar la validación de estado de stock como propiedad dentro del modelo siguiendo las restricciones técnicas.
    @property
    def estado_stock(self) -> str:
        """Retorna el estado operativo del inventario para el producto."""
        if self.stock == 0:
            return "Agotado"
        if self.stock < 5:
            return "Stock Crítico"
        return "Disponible"

    def __str__(self) -> str:
        return f"{self.nombre} ({self.categoria}) - S/ {self.precio}"
