# Sistema de Catálogo de Productos - Django 6.1.3 (Arquitectura MTV)

Laboratorio de la Semana 11 de la asignatura Desarrollo de Aplicaciones Web (IS093A), implementando el patrón arquitectónico Model-Template-View (MTV) con Django 5.x y persistencia mediante ORM en SQLite.

## 1. Arquitectura MTV Implementada
* **Model (`catalogo/models.py`):** Definición de la entidad `Producto` mapeada mediante el ORM de Django hacia SQLite, delegando las reglas de negocio (evaluación de stock crítico) directamente al modelo.
* **Template (`catalogo/templates/`):** Sistema de plantillas desacoplado con herencia estructural (`base.html`), bloques dinámicos (`{% block %}`), etiquetas de control (`{% for %}`, `{% if %}`), resolución inversa de rutas (`{% url %}`) y filtros de transformación (`|title`, `|date`).
* **View (`catalogo/views.py`):** Implementación híbrida combinando Vistas Basadas en Funciones (`home` - FBV) y Vistas Basadas en Clases (`ProductoListView` - CBV heredando de `ListView`).

## 2. Mapa de Enrutamiento (URLs)
| Nombre de Ruta (`name`) | Endpoint | Tipo de Vista | Propósito |
| :--- | :--- | :--- | :--- |
| `home` | `/` | FBV (`def home`) | Resumen estadístico de registros mediante consultas ORM. |
| `catalogo` | `/productos/` | CBV (`ProductoListView`) | Renderizado tabular de productos activos ordenados por fecha. |

## 3. Comandos de Despliegue Local
1. Crear y activar entorno virtual:
   `python -m venv venv` y `venv\Scripts\activate`
2. Instalar dependencias:
   `pip install -r requirements.txt`
3. Validar configuración y aplicar migraciones ORM:
   `python manage.py check`
   `python manage.py migrate`
4. Iniciar servidor de desarrollo:
   `python manage.py runserver`

## 4. Evidencias de Ejecución
Todas las capturas de pantalla correspondientes a los 5 pasos de la guía práctica se encuentran documentadas en el informe técnico adjunto a este repositorio (el archivo `db.sqlite3` ha sido excluido mediante `.gitignore` siguiendo las normas de laboratorio).