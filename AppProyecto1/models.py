from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name=models.CharField(max_length=40)
    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=models.TextField()
    tag=models.ManyToManyField(Tag) #Este many to many crea la tabla blog_tag en la base
    def __str__(self):
        return self.title

class Comment(models.Model):
    text=models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) #el casacade hace q si se borra un usuario, en consecuencia se borre el avatar
    imagen = models.ImageField(upload_to='avatares', null=True, blank=True) #se guarda en la carpeta media, las imagenes cargadas
    descripcion = models.TextField()
    link = models.URLField()
    
    def __str__(self):
        return f"Avatar de: {self.user.username}"