from django.urls import path
from AppBabys.views import *

urlpatterns = [
    
    path("inicio", inicio, name="inicio"),
    path("bodys", bodys, name="bodys"),
    path("pantalones", pantalones, name="pantalones"),
    path("remeras", remeras, name="remeras"),
    path("resultadoBusqueda", resultadoBusqueda, name="resultadoBusqueda"),
    path("buscarProductos", buscarProductos, name="buscarProductos"),
    path("", inicio, name="inicio"),
]
