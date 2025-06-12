from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Equipo, Jugador, Campeonato, CampeonatoEquipos

# Recursos para cada modelo con django-import-export

class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo

class JugadorResource(resources.ModelResource):
    class Meta:
        model = Jugador

class CampeonatoResource(resources.ModelResource):
    class Meta:
        model = Campeonato

class CampeonatoEquiposResource(resources.ModelResource):
    class Meta:
        model = CampeonatoEquipos


class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = EquipoResource
    list_display = ('nombre', 'siglas', 'username_twitter')
    search_fields = ('nombre', 'siglas', 'username_twitter')

class JugadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = JugadorResource
    list_display = ('nombre', 'posicion_campo', 'numero_camiseta', 'sueldo', 'equipo')
    search_fields = ('nombre', 'posicion_campo', 'equipo__nombre')

class CampeonatoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CampeonatoResource
    list_display = ('nombre', 'auspiciante')
    search_fields = ('nombre', 'auspiciante')

class CampeonatoEquiposAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = CampeonatoEquiposResource
    list_display = ('anio', 'equipo', 'campeonato')
    search_fields = ('anio', 'equipo__nombre', 'campeonato__nombre')

# Registrar los modelos en el admin de Django

admin.site.register(Equipo, EquipoAdmin)
admin.site.register(Jugador, JugadorAdmin)
admin.site.register(Campeonato, CampeonatoAdmin)
admin.site.register(CampeonatoEquipos, CampeonatoEquiposAdmin)
