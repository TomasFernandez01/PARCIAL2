from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API Libros",
        default_version='v1',
        description="API para gestión de libros",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@libros.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='inicio'),
    path('', include('loginApp.urls')),
    path('', include('contacto.urls')),
    path('', include('tareas.urls')),
    path('', include('tareas_CBV.urls')),
    path('', include('galeria.urls')),
    path('', include('informes.urls')),
    path('', include('shop.urls')),
    path('api/', include('api_libros.urls')),
    path('', include('scraper.urls')),
    path('', include('estadisticas.urls')),

    # Swagger URLs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    
]

