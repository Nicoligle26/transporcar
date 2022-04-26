from django.shortcuts import render
from django.http import HttpResponse
from personas.models import User
from vehiculos.models import Vehiculo

# Create your views here.


def index(request):
    return render(request, 'home.html')


def list(request):
    users = User.objects.all()
    data = {'users': users}
    return render(request, 'listado_user.html', data)


def getvehiculos(request):
    id = request.GET.get('cliente')
    vehiculos = Vehiculo.objects.filter(usuario_id=id)
    data = {'vehiculos': vehiculos, 'id': id}
    return render(request, 'listado_user.html', data)
