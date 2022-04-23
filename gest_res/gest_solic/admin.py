from django.contrib import admin
from django.http import HttpRequest
from gest_solic.models import cambioapart
from gest_usuario.models import Estudiantes
# Register your models here.

@admin.register(cambioapart)
class cambioapartAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'usuario', 'ubicacion', 'motivo')
    #ordering = ('nombre',)
    search_fields = ('nombre','apellidos', 'usuario', 'ubicacion')
    #list_display_links = ('nombre',)
    #list_filter = ('date', 'edif', 'paso', 'apto', 'evaluacion')
    list_per_page = 40
    exclude = ('nombres', 'apellidos', 'usuario', 'ubicacion')

    def get_queryset(self, request: HttpRequest):
        older = super().get_queryset(request)
        if request.user.groups.filter(name='Estudiante').exists():
            return older.filter(usuario=request.user.username)
        return older
    
    def save_model(self, request: HttpRequest, obj: cambioapart, form, change) -> None:
        est:Estudiantes = Estudiantes.objects.filter(usuario=request.user.username).first()
        obj.nombres = est.nombres
        obj.apellidos = est.apellidos
        obj.usuario = est.usuario
        obj.ubicacion = est.ubicacion
        return super().save_model(request, obj, form, change)