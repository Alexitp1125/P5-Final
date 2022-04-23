from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from gest_usuario.models import Estudiantes,User
from django.http import HttpRequest
# Register your models here.


admin.site.unregister(User)



@admin.register(User)
class UserAdmin(UserAdmin):
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Permissions'), {
            'fields': ('groups',),
        }),
        
    )
    list_display = ('first_name','last_name','username', 'is_active')
    list_filter = ('is_active', 'groups')
    search_fields = ('username','first_name','last_name')
    ordering = ('username',)
    filter_horizontal = ('groups',)
    
    def save_model(self, request: HttpRequest, obj, form, change) -> None:
        if not change:
            obj.is_staff = True
        return super().save_model(request, obj, form, change)



@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellidos', 'usuario', 'ubicacion')
    #ordering = ('nombre',)
    search_fields = ('nombres', 'usuario', 'ubicacion')
    #list_display_links = ('nombre',)
    #list_filter = ('nombres', 'usuario','ubicacion')
    list_per_page = 40
    exclude = ('nombres', 'apellidos', 'usuario', 'contrasena', 'categoria')