from django.db import models

# Create your models here.

class cambioapart(models.Model):
    nombres = models.CharField(db_column='Nombres',verbose_name="Nombre(s)", max_length=100)
    apellidos =  models.CharField(db_column='Apellidos', verbose_name="Apellidos", max_length=100)
    usuario = models.CharField(db_column='Usuario', verbose_name="usuario",max_length=100)  
    ubicacion = models.PositiveBigIntegerField(db_column='Ubicacion') 
    motivo = models.TextField(db_column='motivo')

    
    def __str__(self) -> str:
        return self.nombres

    class Meta:
        verbose_name = 'Solicitud Cambio de Apartamento'
        verbose_name_plural = 'Solicitudes'
        db_table = 'Solicitudes'