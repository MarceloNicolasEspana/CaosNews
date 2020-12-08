from django.db import models

# Create your models here.

#Clase para ingresar datos de usuarios X en la base de datos.
class Usuario(models.Model):
    nombre=models.CharField(max_length=50, verbose_name='nombre')
    email=models.CharField(max_length=30, verbose_name='email')
    contraseña=models.CharField(max_length=20, verbose_name='contraseña', null=False)


#Clase para ingresar datos de periodistas en la bbdd
class Periodista(models.Model):
    idPeriodista=models.AutoField(primary_key=True, verbose_name='id periodista')
    nombre=models.CharField(max_length=50, verbose_name='nombre periodista')
    email=models.CharField(max_length=20, verbose_name='email periodista')
    foto=models.CharField(max_length=20, verbose_name='foto periodista')
    contraseña=models.CharField(max_length=10, verbose_name='contraseña periodista')

    def __str__(self):
        return '{0},{1}'.format(self.nombre, self.email)
    


#Clases para poder ingresar noticias según categoria.
class Categoria(models.Model):
    idCategoria=models.AutoField(primary_key=True, verbose_name='id categoria')
    nombreCategoria=models.CharField(max_length=30, verbose_name='nombre categoria')


class Noticia(models.Model):
    idNoticia=models.AutoField(primary_key=True, verbose_name='id noticia')
    titulo=models.CharField(max_length=20, verbose_name='titulo noticia')
    descripcion=models.CharField(max_length=200, verbose_name='descripcion noticia')
    fecha=models.DateField(verbose_name='fecha publicacion')
    imagen=models.CharField(max_length=20, verbose_name='imagen noticia')
    idCategoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)
    idPeriodista=models.ForeignKey(Periodista, on_delete=models.CASCADE)


