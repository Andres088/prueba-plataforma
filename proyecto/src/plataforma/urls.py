from django.contrib import admin
from django.urls import path
from .views import home_page
from iniciativa.views import registro_iniciativa


urlpatterns = [
    path('', home_page),
    path('registro-iniciativa/', registro_iniciativa),
    path('admin/', admin.site.urls),
]
