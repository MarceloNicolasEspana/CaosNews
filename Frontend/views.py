from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import models

# Create your views here.

def Index(request):
    noticia=models.Noticia.objects.all()
    datos={"noticias": noticia}
    return render(request,'index.html', datos)

def Articulo(request, id):
    articulo = models.Noticia.objects.get(idNoticia = id)
    datos = {"articulo":articulo}
    return render(request, 'articulo.html',datos)

def Nosotros(request):
    return render(request,'nosotros.html')   

def IndexDos(request):
    noticia=models.Noticia.objects.all()
    datos={"noticias": noticia}
    return render(request,'index2.html', datos)


def RegForm(request):
    return render(request, 'form_registro.html')    



def GuardaUsuario(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        email=request.POST.get('email')
        contraseña=request.POST.get('pass')

        nuevoUsuario = models.Usuario()
        nuevoUsuario.nombre=nombre
        nuevoUsuario.email=email
        nuevoUsuario.contraseña=contraseña

        nuevoUsuario.save()
        return render(request, 'registrado.html')


@login_required
def IndexAdmin(request):
    noticia=models.Noticia.objects.all()
    datos={"noticias": noticia}
    return render(request,'indexAdmin.html', datos)   
