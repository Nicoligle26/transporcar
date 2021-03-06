"""transporcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from vehiculos.views import list, create, delete, parcial_final, reporte_pdf
from personas.views import getUsers, getVehiculos
from reparaciones.views import show, listado_pdf, taller_final
urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehiculos/', list),
    path('', getUsers),
    path('list_user/', getVehiculos),
    path('reparacion/<id>', show),
    path('infracciones/', create),
    path('eliminar_vehiculo/', delete),
    path('lista_pdf', listado_pdf),
    path('taller_final/', taller_final),
    path('parcial_final/', parcial_final),
    path('reporte_pdf/<id>', reporte_pdf),
]
