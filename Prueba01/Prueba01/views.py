from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.template import loader 
from django.shortcuts import render
import datetime 

def saludo(request):
    nombre="Jack"
    apellido= "Eksteen"
    temas=["Plantillas","Modelos","Formularios","Vistas"]
    fecha = datetime.datetime.now()
    return render(request,"plantilla.html",{"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha, "temas_curso":temas})

def saludo_html(request):
    documento="""<html><body><h1>Hola Mundo!</h1></body></html>"""
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("Hasta Luego Mudno!")

def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>La fecha actual es: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(documento)

def curso(request):
    fecha = datetime.datetime.now()
    return render(request, "curso.html",{"now":fecha})

def calcular_edad(request,edad,ano):
    periodo=ano-2023
    edad_futura=edad+periodo
    documento="<html><body><h1>en el año %s tendras %s años</h1></body></html>"%(ano,edad_futura)
    return HttpResponse(documento)