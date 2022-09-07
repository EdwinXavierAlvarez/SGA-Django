from django.db import models

from applications.usuario.models import ModeloBase

# Create your models here.
class Administrativo(ModeloBase):
    persona = models.ForeignKey("core.persona", on_delete=models.CASCADE, verbose_name='Persona')
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso')
    activo = models.BooleanField(default=True , verbose_name='Activo')
    contrato = models.CharField(max_length=50, null=True, blank=True, verbose_name='Contrato')
    
    class Meta:
        verbose_name = 'Administrativo'
        verbose_name_plural = 'Administrativos'
        ordering = ['persona__nombres']