from django.db import models

# Create your models here.

class cuart(models.Model):
    name = models.CharField(verbose_name="Nombre(s)", max_length=100)
    lastname = models.CharField(verbose_name="Apellidos", max_length=100)
    usuario = models.CharField(db_column='Usuario', verbose_name="usuario",max_length=100,default=0)
    date = models.DateField()
    edif = models.PositiveSmallIntegerField(verbose_name='Edificio')
    paso = models.PositiveSmallIntegerField(verbose_name='Paso')
    apto = models.PositiveSmallIntegerField(verbose_name='Apto')

    Bien = 'Bien'
    Regular = 'Regular'
    Mal = 'Mal'
    
    list_eval = (
        (Bien, 'Bien'),
        (Regular, 'Regular'),
        (Mal, 'Mal'),

    )
    Evaluacion = models.TextField(verbose_name='Eval',choices=list_eval,null=True,blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Cuarteleria'
        verbose_name_plural = 'Cuartelerias'
        db_table = 'cuarteleria'
        ordering = ['id']