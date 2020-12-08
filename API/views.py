from django.shortcuts import render
from rest_framework import generics
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic.edit import FormView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from Frontend import models
from .serializers import PeriodistaSerializer
# Create your views here.

class PeriodistaList(generics.ListCreateAPIView):
    queryset = models.Periodista.objects.all()
    serializer_class = PeriodistaSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)



class Login(FormView):
    template_name = "login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('loginadm:login_adm')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,**kwargs)

def form_valid(self,form):
    user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
    token,_ = Token.objects.get_or_create(user = user)
    if token:
        login(self.request, form.get_user())
        return super(Login,self).form_valid(form)


