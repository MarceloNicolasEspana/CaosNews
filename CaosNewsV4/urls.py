"""CaosNewsVersion2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from Frontend import views as views_front
from Backend import views as views_back
from API.views import Login
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views as token_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexAdmin/', views_front.IndexAdmin),
    path('index/', views_front.Index),
    path('nosotros/', views_front.Nosotros),
    path('indexdos/', views_front.IndexDos),
    path('registroUsuario/', views_front.RegForm),
    path('guardaUsuario/', views_front.GuardaUsuario),
    path('articulo/<int:id>/',views_front.Articulo),
    #Periodistas
    path('adminPeriodista/', views_back.admin),
    path('registrarPeriodista/', views_back.form_periodista),
    path('listarPeriodista/', views_back.listarPeriodista),
    path('modificarPeriodista/<int:id>/', views_back.modificarPeriodista, name="modifiPeriodista"),
    path('eliminarPeriodista/<int:id>/', views_back.eliminarPeriodista, name ="eliminarPeriodista"),
    path('login/<str:nombre>/<str:contraseña>/', views_back.login, name="login"),
    #Noticias
    path('indexPeriodista/', views_back.indexPeriodista),
    path('formArticulo/', views_back.form_noticia),
    path('listarnoticia/', views_back.listarnoticias),
    path('modificarNoticia/<int:id>/', views_back.modificarNoticia, name="modifinoticia"),
    path('eliminarNoticia/<int:id>/', views_back.eliminarnoticia, name ="eliminarnoticia"),
    #Sesion
    path('loginPe/', auth_views.LoginView.as_view(template_name='loginPeriodista.html'), name = 'loginPeriodista'),
    path('loginadmin', include(('API.urls','loginadm'))),
    path('login/', auth_views.LoginView.as_view(template_name='log_in.html'), name='login' ),
    path('logindos/', views_back.login, name = 'loginperiodista'),
    #path('logout/', auth_views.LogoutView.as_view(template_name='log_in.html'), name='logout' ),
    #Path API
    path('api/v1/', include('API.urls')),
    path('api_generate_token/', token_views.obtain_auth_token),
    path('loginn/', Login.as_view(), name = 'loginn'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('allauth.urls')),
    #buscador
    path('buscar/', views_back.buscar),
    path('buscarArticulo/', views_back.buscarArticulo),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)