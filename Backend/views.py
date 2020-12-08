from django.shortcuts import render
from Frontend import models
from datetime import datetime 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .forms import PeriodistaForm, LoginForm, NoticiaForm

# Create your views here.

#Todo sobre periodista

@login_required(login_url = '/login/')
def indexPeriodista(request):
      if request.user.is_authenticated:
       return render(request,'indexPeriodista.html')
      else:
            return render(request,'loginPeriodista.html')

#Crear periodista
def admin(request):
      if request.user.is_authenticated:
         return render(request,'admin.html')
      else:
         return render(request, 'log_in.html')     


def form_periodista(request):
      if request.method=="GET":
        form = PeriodistaForm()
        datos = {'form':form}
        return render(request,'form_periodista.html', datos)
      else:
        form = PeriodistaForm(request.POST)
        datos = {'form':form}
        if form.is_valid():
              form.save()
              return render(request,'registrado.html', datos)
        
      
#Listar periodistas.
def listarPeriodista(request):
  periodistas = models.Periodista.objects.all()
  datos = {'periodistas': periodistas}
  return render (request, 'listar_periodista.html', datos)   


#Modificar Periodista

def modificarPeriodista(request,id):
  periodista = models.Periodista.objects.get(idPeriodista=id)
  if request.method=="GET":
        form = PeriodistaForm(instance = periodista)
        datos = {'form':form}
        return render(request,'form_periodista.html', datos)
  else:
    form = PeriodistaForm(request.POST, instance = periodista)    
    if form.is_valid():
       form.save()
       return render(request,'registrado.html')  

#Eliminar periodista

def eliminarPeriodista(request, id):
      periodista = models.Periodista.objects.get(idPeriodista=id)
      periodista.delete()
      return render(request,'eliminado.html')


#NOTICIAS

#crear noticia
def form_noticia(request):
  if request.method=="GET":
        form = NoticiaForm()
        datos = {'form':form}
        return render(request,'form_articulo.html', datos)
  else:
     form = NoticiaForm(request.POST)
     datos = {'form':form}
     if form.is_valid():
        form.save()
        return render(request, 'registrado.html', datos)         
      
#Listar noticia
def listarnoticias(request):
  noticias = models.Noticia.objects.all()
  datos = {'noticias': noticias}
  return render (request, 'listar_noticias.html', datos)   


#Modificar noticia

def modificarNoticia(request,id):
  noticia = models.Noticia.objects.get(idNoticia=id)
  if request.method=="GET":
        form = NoticiaForm(instance = noticia)
        datos = {'form':form}
        return render(request,'form_articulo.html', datos)
  else:
    form = NoticiaForm(request.POST, instance = noticia)    
    if form.is_valid():
       form.save()
       return render(request,'registrado.html')  

#Eliminar noticia

def eliminarnoticia(request, id):
      noticia = models.Noticia.objects.get(idNoticia=id)
      noticia.delete()
      return render(request,'eliminado.html')


#LogOut

def logout(request):
      logout(request)
      return HttpResponseRedirect('/loginPeriodista/')


def login(request):
      if request.method=='POST':
         form = AuthenticationForm(data=request.POST)
         if form.is_valid():
               username = form.cleaned_data['username']
               password = form.cleaned_data['password']

               user = authenticate(username = username, password = password)
               return HttpResponseRedirect('/indexPeriodista/')

               if user is not None:
                     login(request, user)

                     return HttpResponseRedirect('/indexPeriodista/')

         return render(request, 'login.html', {'form':form})          


#buscador

def buscar(request):
      queryset = models.Periodista.objects.all()
      nombre_query = request.GET.get('nombre')

      if nombre_query != '' and nombre_query is not None:
            queryset = queryset.filter(nombre = nombre_query)

      datos = {'queryset':queryset}
      return render(request, 'buscador.html', datos)


#Buscador de articulo
def buscarArticulo(request):
      queryset = models.Noticia.objects.all()
      titulo_query = request.GET.get('titulo')

      if titulo_query != '' and titulo_query is not None:
            queryset = queryset.filter(titulo = titulo_query)

      datos = {'queryset':queryset}
      return render(request, 'buscadorArticulo.html', datos)
