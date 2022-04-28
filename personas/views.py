from django.shortcuts import render
from django.http import HttpResponse
from personas.models import User
from vehiculos.models import Vehiculo

# Create your views here.


def index(request):
    return render(request, 'home.html')


def getUsers(request):
    users = User.objects.all()
    data = {'users': users}
    return render(request, 'listado_user.html', data)


def getVehiculos(request):
    id = request.POST.get('cliente')
    users = User.objects.all()
    if request.method == 'POST':
        vehiculos = Vehiculo.objects.filter(usuario=id)
        data = {'vehiculos': vehiculos, 'id': id, 'users': users}
        return render(request, 'listado_user.html', data)
