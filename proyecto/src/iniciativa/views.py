from django.shortcuts import render
from .models import Iniciativa
from .forms import IniciativaModelForm


def registro_iniciativa(request):

    form = IniciativaModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = IniciativaModelForm()

    template_name = 'registro-iniciativa.html'
    context = {'form': form}
    
    return render(request, template_name, context)


