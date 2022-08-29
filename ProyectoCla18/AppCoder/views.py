from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(request):
    curso = Curso(nombre = 'python', comision = 31105)
    curso.save()
    texto = f'Curso creado. Nombre es {curso.nombre} y comision es {curso.comision}'
    return HttpResponse(texto)