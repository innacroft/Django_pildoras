
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template

import datetime


class Persona(object):

  def __init__(self, nombre,apellido):
    self.nombre=nombre
    self.apellido=apellido

def saludo(request): #primera vista
  p1=Persona("Juan", "Diaz")
  temas=["django","python", "web", "basesdatos"]
  #ctx=Context({"nombre":p1.nombre, "apellido": p1.apellido ,"temas":temas})
  #doc_ext= get_template('templ_persona.html')
  #documento=doc_ext.render({"nombre":p1.nombre, "apellido": p1.apellido ,"temas":temas})
  return render(request,'templ_persona.html',{"nombre":p1.nombre, "apellido": p1.apellido ,"temas":temas})

def damefecha(request):
  date= datetime.datetime.now()
  return render(render,'feed.html', date)

def feedClass(request):
  date= datetime.datetime.now()
  return render(request,'feed.html', {"dameFecha":date})

def pagCurso(request):
  date= datetime.datetime.now()
  return render(request,'pagcurso.html', {"dameFecha":date})
