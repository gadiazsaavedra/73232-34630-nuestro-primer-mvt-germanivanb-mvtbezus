from django.http import HttpResponse
from django.shortcuts import render

from .models import Familiares

# Create your views here.


def info(request, nombre, fecha, agno):

    datos = Familiares(nombre=nombre, fecha=fecha, agno=agno)
    datos.save()

    return HttpResponse(
        f"""
    <p> La persona: {datos.nombre}, nació el: {datos.fecha} y tiene {datos.agno}. Agregado con éxito! </p>
    """
    )


def lista_familiares(request):

    lista = Familiares.objects.all()

    return render(request, "lista_familia.html", {"lista_familia": lista})
