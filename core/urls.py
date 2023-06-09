from django.urls import path 
from .views import home, poleras, pantalones, polerones, about, registro, formulario_tienda


urlpatterns = [
    path('', home, name="home"),
    path('poleras', poleras, name="poleras"),
    path('pantalones', pantalones, name="pantalones"),
    path('polerones', polerones, name = "polerones"),
    path('about', about, name = "about"),
    path('registro', registro, name = "registro"),
    path('formulario_tienda', formulario_tienda, name = "formulario_tienda"),   
]