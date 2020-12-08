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
from rest_framework import routers
from django.urls import path
from API import viewsets
from .views import Login
from Backend import views as views_back
from .views import PeriodistaList

router = routers.SimpleRouter()
router.register('Usuario', viewsets.UsuarioViewSet)

urlpatterns = router.urls
    #path('periodista/', PeriodistaList.as_view(), name = 'periodista_list'),
    #path('adminPeriodista/', views_back.admin, name = 'admperiodista'),
    #path('loginadm/', Login.as_view(), name = 'login_adm'),

