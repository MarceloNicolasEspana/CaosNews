from django import forms
from Frontend import models

class PeriodistaForm(forms.ModelForm):
    class Meta:
        model = models.Periodista
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = models.Periodista
        fields = ('nombre', 'contraseña')


class NoticiaForm(forms.ModelForm):
    class Meta:
        model = models.Noticia
        fields = '__all__'