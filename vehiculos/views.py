from django.shortcuts import render
from django.http import HttpResponse
from reparaciones.models import Vehiculo


# Create your views here.
def index(request):
    return render(request, 'home.html')


def list(request):
    vehiculos = Vehiculo.objects.all()
    data = {'vehiculos': vehiculos}
    return render(request, 'listado_vehiculo.html', data)
