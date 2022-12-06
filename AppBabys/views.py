from django.shortcuts import render
from AppBabys.forms import *
from AppBabys.models import *


def inicio(request):
    return render(request, "inicio.html", {"mensaje_inicio": "Hola, estas en inicio"})


def bodys(request):
    if request.method == "POST":
        formulario_bodys = FormBodys(request.POST)
        if formulario_bodys.is_valid():
            formulario_limpia = formulario_bodys.cleaned_data
            bodys_ingresado_db = Bodys(marca=formulario_limpia["marca"], modelo=formulario_limpia["modelo"],
                                           color=formulario_limpia["color"], talle=formulario_limpia["talle"], precio=formulario_limpia["precio"])
            bodys_ingresado_db.save()
            return render(request, "inicio.html", {"mensaje_inicio": "Datos GuardadosS!"})
    else:
        formulario_bodys_vacio = FormBodys()
        return render(request, "bodys.html", {"bodys" : formulario_bodys_vacio})
   


def remeras(request):
    if request.method == "POST":
        formulario_remeras = FormRemeras(request.POST)
        if formulario_remeras.is_valid():
            formulario_limpia = formulario_remeras.cleaned_data
            remeras_ingresado_db = Remeras(marca=formulario_limpia["marca"], modelo=formulario_limpia["modelo"],
                                           color=formulario_limpia["color"], talle=formulario_limpia["talle"], precio=formulario_limpia["precio"])
            remeras_ingresado_db.save()
            return render(request, "inicio.html", {"mensaje_inicio": "Datos GuardadosS!"})
    else:
        formulario_remeras_vacio = FormRemeras()
        return render(request, "remeras.html", {"remeras" : formulario_remeras_vacio})

def pantalones(request):
    if request.method == "POST":
        formulario_pantalones = FormPantalones(request.POST)
        if formulario_pantalones.is_valid():
            formulario_limpia = formulario_pantalones.cleaned_data
            pantalones_ingresado_db = Pantalones(marca = formulario_limpia["marca"], modelo = formulario_limpia["modelo"], color = formulario_limpia["color"], talle = formulario_limpia["talle"], precio = formulario_limpia["precio"])
            pantalones_ingresado_db.save()
            return render(request, "inicio.html", {"mensaje_inicio":"Datos GuardadosS!"})
    else:
        formulario_pantalones_vacio = FormPantalones()
        return render(request, "pantalones.html", {"pantalones" : formulario_pantalones_vacio})
    
def buscarProductos(request):
    return render(request, "buscarProductos.html", {"mensaje_inicio": "Buscar Productos"})
    
"""def buscar(request):    
    if request.Get["tipo"]:
        tipo=request.Get["tipo"]        
        tipo=tipo.objets.filter(tipo=)
        return render(request, "resultadobuscar.html", {"prductos": "productos" })
    else:
        return render(request, "buscarProductos.html", {"mensaje_inicio: "Buscar Productos"})"""