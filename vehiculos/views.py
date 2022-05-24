from django.shortcuts import redirect, render
from django.http import HttpResponse
from reparaciones.models import Vehiculo, Reparacion
from vehiculos.models import Infraccion
from personas.models import Conductor, User

# Create your views here.


def index(request):
    return render(request, 'home.html')


def list(request):
    vehiculos = Vehiculo.objects.all()
    data = {'vehiculos': vehiculos}
    return render(request, 'listado_vehiculo.html', data)


def create(request):
    conductores = Conductor.objects.all()
    vehiculos = Vehiculo.objects.all()
    if request.method == 'POST':
        infraccion = Infraccion()
        infraccion.fecha = request.POST.get('fecha')
        infraccion.descripcion = request.POST.get('observacion')
        infraccion.valor = request.POST.get('valor')
        infraccion.conductor = Conductor.objects.get(
            id=request.POST.get('conductor'))
        infraccion.vehiculo = Vehiculo.objects.get(
            id=request.POST.get('vehiculo'))
        infraccion.save()
        print('El registro ha sido guardado')
    msg = 'La infraccion ha sido guardada'
    data = {'conductores': conductores, 'vehiculos': vehiculos, 'msg': msg}
    return render(request, 'registrar_infraccion.html', data)


def delete(request, id):
    vehiculo = Vehiculo.objects.get(id=id)
    vehiculo.placa
    vehiculo.delete()
    vehiculos = Vehiculo.objects.all()
    data = {'vehiculos': vehiculos}
    return render(request, 'lista_vehiculo.html', data)
