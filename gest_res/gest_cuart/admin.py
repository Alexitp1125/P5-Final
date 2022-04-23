from django.contrib import admin
from gest_cuart.models import cuart
from django.http import HttpRequest
# Register your models here.


@admin.register(cuart)
class cuartAdmin(admin.ModelAdmin):
    list_display = ('name', 'lastname', 'date', 'edif', 'paso', 'apto', 'Evaluacion')
    #ordering = ('nombre',)
    search_fields = ('name','lastname','Evaluacion', 'date')
    #list_display_links = ('nombre',)
    list_filter = ('date', 'edif', 'paso', 'apto', 'Evaluacion')
    list_per_page = 40
    #exclude = ('name', 'lastname', 'date', 'edif', 'paso', 'apto')
    def get_queryset(self, request: HttpRequest):
        older = super().get_queryset(request)
        if request.user.groups.filter(name='Estudiante').exists():
            older = older.filter(usuario=request.user.username)
        return older.order_by('date')