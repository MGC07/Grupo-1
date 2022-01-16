from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AppProyecto1 import views

urlpatterns = [
    path('',views.blogs, name='Blog'),
    path('comment/<id>',views.comment, name='Comment'),
    path('showBlog/<id>',views.showBlog, name='ShowBlog'),
    path("busquedaBlog/",views.busquedaBlog, name ="BusquedaBlog"),
    path("buscar/",views.buscar, name ="Buscar"),
]