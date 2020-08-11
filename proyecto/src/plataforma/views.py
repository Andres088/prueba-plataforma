from django.shortcuts import render
from iniciativa.models import Iniciativa



# Model View Template (MVT)

def home_page(request):
    qs = Iniciativa.objects.all()
    context = {"lista_iniciativas": qs}
    return render(request, 'home.html', context)




