from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AppProyecto1 import views

urlpatterns = [
    # path('',views.blogs, name='Blog'),
    path('',views.inicio, name="inicio"),
    path('padre',views.padre, name="padre"), # Esta es para ver la página padre
    path('index',views.index, name="index"), # Esta es para ver la planilla original completa

    path('blogs',views.blogs, name="blogs"),

    path('showBlog/<id>',views.showBlog, name='showBlog'), # No funciona porque pide id
    path('comment/<id>',views.comment, name='Comment'), # No funciona porque pide id

]