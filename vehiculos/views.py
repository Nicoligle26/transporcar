from django.shortcuts import redirect, render
from django.http import HttpResponse
from reparaciones.models import Vehiculo
from vehiculos.models import Infraccion
from personas.models import Conductor, User

# PDF
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
import os

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

# PDF Methods


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def reporte_pdf(request, id):
    infracciones = Infraccion.objects.filter(vehiculo=id)
    vehiculo = Vehiculo.objects.get(id=id)
    sum = 0
    for i in infracciones:
        sum += i.valor

    data = {'infracciones': infracciones, 'vehiculo': vehiculo, 'total': sum}
    pdf = render_to_pdf('pdf/reporte_pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')


def parcial_final(request):
    usuarios = User.objects.all()
    conductores = Conductor.objects.all()
    data = {'conductores': conductores, 'usuarios': usuarios}
    if request.method == 'POST':
        usuario_id = request.POST.get('cliente')
        conductor_id = request.POST.get('conductor')
        vehiculos = Vehiculo.objects.filter(
            usuario=usuario_id, conductor=conductor_id)
        data = {'conductores': conductores,
                'usuarios': usuarios, 'vehiculos': vehiculos}
        return render(request, 'parcial_final.html', data)
    else:
        return render(request, 'parcial_final.html', data)
