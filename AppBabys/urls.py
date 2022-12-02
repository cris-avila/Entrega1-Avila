from django.urls import path
from AppBabys.views import *

urlpatterns = [
    
    path("inicio", inicio, name="inicio"),
    path("bodys", bodys, name="bodys"),
    path("pantalones", pantalones, name="pantalones"),
    path("remeras", remeras, name="remeras"),
    path("buscar", buscar, name="buscar"),
    path("", inicio, name="inicio"),
]
