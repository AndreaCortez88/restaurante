from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class ResourceBebidas(resources.ModelResource):
    class Meta:
        model = Bebidas

class AdminBebidas(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_bebidas', 'codigo', 'nombre', 'descripcion', 'precio']
    resource_class = ResourceBebidas

admin.site.register(Bebidas, AdminBebidas)

class ResourcePostres(resources.ModelResource):
    class Meta:
        model = Postres

class AdminPostres(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_post']
    list_display = ['pk_postres', 'codigo_post', 'nombre_post', 'descripcion_post', 'precio_post']
    resource_class = ResourcePostres

admin.site.register(Postres, AdminPostres)

class ResourceExtras(resources.ModelResource):
    class Meta:
        model = Extras

class AdminExtras(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre_ext']
    list_display = ['pk_extras', 'codigo_ext', 'nombre_ext', 'descripcion_ext', 'precio_ext']
    resource_class = ResourceExtras

admin.site.register(Extras, AdminExtras)