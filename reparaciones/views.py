from django.shortcuts import render
from django.http import HttpResponse
from reparaciones.models import Reparacion, Detalle

# Create your views here.

def index(request):
    return render(request, 'home.html')

def show(request, id):
    reparacion = Reparacion.objects.filter(vehiculo=id).last()
    detalles = Detalle.objects.filter(reparacion=reparacion)
    data = {'reparacion': reparacion, 'detalles': detalles}
    return render(request, 'reparacion.html', data)
