from re import search
from django.contrib import admin
from personas.models import User, Conductor

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'direccion', 'telefono', 'correo')
    list_filter = ('apellidos',)
    search_fields = ('nombres', 'apellidos',)


admin.site.register(User, UserAdmin)


class ConductorAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'direccion', 'telefono', 'correo')
    list_filter = ('apellidos',)
    search_fields = ('nombres', 'apellidos',)


admin.site.register(Conductor, ConductorAdmin)
