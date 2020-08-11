from django import forms
from .models import Iniciativa


class IniciativaModelForm(forms.ModelForm):

    class Meta:
        model = Iniciativa
        fields = [
            'nro_correlativo',
            'eje_estrategico',
            'requerimiento',
            'fecha_solicitud',
            'fecha_solped',
            'nombre',
            'descripcion',
            'objetivo',
            'beneficio',
            'impacto',
            'inicio',
            'fin',
            'sponsor',
            'solicitante',
            'capa_red',
            'ubicacion',
            'tipo']

