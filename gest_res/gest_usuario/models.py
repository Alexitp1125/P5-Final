from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Estudiantes(models.Model):
    nombres = models.TextField(db_column='Nombres', blank=True, null=True)  # Field name made lowercase.
    apellidos = models.TextField(db_column='Apellidos', blank=True, null=True)  # Field name made lowercase.
    usuario = models.TextField(db_column='Usuario', blank=True, null=True)  # Field name made lowercase.
    contrasena = models.TextField(blank=True, null=True)
    categoria = models.TextField(db_column='Categoria', blank=True, null=True)  # Field name made lowercase.
    ubicacion = models.PositiveBigIntegerField(db_column='Ubicacion', blank=True, null=True)  # Field name made lowercase.

    def __str__(self) -> str:
        return self.nombres

    class Meta:
        # managed = False
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'
        db_table = 'estudiantes'
        ordering = ['id']   