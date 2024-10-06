from django.urls import path
from inicio.views import mi_vista, inicio, vista_datos1, primer_template, segundo_template, crear_auto

urlpatterns = [
    path('mi-vista/', mi_vista),
    path('', inicio),
    path('vista-datos1/<nombre>/', vista_datos1),
    path('primer-template/', primer_template),
    path('segundo-template/', segundo_template),
    path('crear_auto/<str:marca>/<str:modelo>/<int:anio>', crear_auto)
]