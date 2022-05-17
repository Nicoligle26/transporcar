from django.shortcuts import render
from django.http import HttpResponse
from reparaciones.models import Reparacion, Detalle
from vehiculos.models import Vehiculo

# PDF
from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template


# Create your views here.


def index(request):
    return render(request, 'index.html')


def show(request, id):
    reparacion = Reparacion.objects.filter(vehiculo=id).last()
    detalles = Detalle.objects.filter(reparacion=reparacion)
    total = 0
    for x in detalles:
        total = total+(x.costo * x.cantidad)
    data = {'reparacion': reparacion, 'detalles': detalles, 'total': total}
    return render(request, 'reparacion.html', data)

# PDF Methods


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def listado_pdf(request):
    vehiculos = Vehiculo.objects.all()
    data = {'vehiculos': vehiculos}
    pdf = render_to_pdf('pdf/vehiculos_pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')
