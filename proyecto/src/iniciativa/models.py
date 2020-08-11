from django.conf import settings
from django.db import models



class Iniciativa(models.Model): 

    nro_correlativo = models.IntegerField(default=1)
    eje_estrategico = models.CharField(default='Capacidad_I_Calidad_de_Servicio', max_length=100, null=True)
    requerimiento = models.CharField(default='Incrementar %X en Capacidad de Transporte', max_length=100, null=True)
    fecha_solicitud = models.DateField(default='2020-08-11', null=True)
    fecha_solped = models.DateField(default='2020-08-11', null=True)
    nombre = models.CharField(default='Iniciativa 1', max_length=75, null=True)
    descripcion = models.TextField(default='Esta iniciativa consiste en...', max_length=240, null=True)
    objetivo = models.TextField(default='El objetivo es...', max_length=300, null=True)
    beneficio = models.TextField(default='Optimizar los procesos...', max_length=500, null=True)
    impacto = models.CharField(default='Retraso en las operaciones del area logistica', max_length=100, null=True)
    inicio = models.DateField(default='2020-09-01', null=True)
    fin = models.DateField(default='2020-09-30', null=True)
    sponsor = models.CharField(default='GERENCIA DE OPERACIONES', max_length=100, null=True)
    solicitante = models.CharField(default='JEFATURA DE PROCESOS INTERNOS', max_length=100, null=True)
    capa_red = models.CharField(default='TRANSPORTE', max_length=50, null=True)
    ubicacion = models.CharField(default='Perú', max_length=100, null=True)
    tipo = models.CharField(default='Reingenieria', max_length=50, null=True)


