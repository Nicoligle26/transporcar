from django.contrib import admin

from reparaciones.models import Detalle, Reparacion, Servicio

# Register your models here.

# class ReparacionAdmin (admin.ModelAdmin):
#     list_display = ('fecha', 'costo', 'descripcion', 'vehiculo')
#     list_filter = ('fecha',)
#     search_fields = ('fecha', 'descripcion',)


# admin.site.register(Reparacion, ReparacionAdmin)


class DetalleAdmin (admin.ModelAdmin):
    list_display = ('costo', 'cantidad', 'servicio', 'reparacion')
    list_filter = ('costo','cantidad',)
    search_fields = ('costo', 'servicio',)


admin.site.register(Detalle, DetalleAdmin)

class ServicioAdmin (admin.ModelAdmin):
    list_display = ('descripcion', 'precio')
    list_filter = ('precio',)
    search_fields = ('descripcion', 'precio',)


admin.site.register(Servicio, ServicioAdmin)

# Maestro detalle
class detalle_reparacion(admin.TabularInline):
    model=Detalle

class ReparacionAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'costo', 'descripcion', 'vehiculo')
    list_filter = ('fecha',)
    search_fields = ('fecha', 'descripcion',)
    inlines = (detalle_reparacion,)

admin.site.register(Reparacion, ReparacionAdmin)
