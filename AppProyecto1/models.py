from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from datetime import datetime

class Tag(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name  

class Blog(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=RichTextField()
    tag=models.ManyToManyField(Tag) #Este many to many crea la tabla blog_tag en la base
    imagen= models.ImageField(upload_to="blogi/",null=True,blank=True)
    fechaCreacion = models.DateTimeField( default=timezone.now)
    publicacion=models.DateTimeField(default=timezone.now ,blank=True, null=True)
    autor= models.ForeignKey(User, on_delete=models.CASCADE,default=None)
       
    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    def __str__(self):
        return self.text

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #el casacade hace q si se borra un usuario, en consecuencia se borre el avatar
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True) #se guarda en la carpeta media, las imagenes cargadas
    descripcion = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return f"Avatar de: {self.user.username}"

# class Mensajeria(models.Model):
#     remitente = models.ForeignKey(User, related_name="remitente")
#     receptor = models.ForeignKey(User, related_name="receptor")
#     contenido = models.TextField()
#     created_at = models.TimeField()