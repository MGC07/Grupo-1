from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AppProyecto1 import views

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('padre',views.padre, name="padre"),
    # Esta es para ver la página padre
    path('index',views.index, name="index"),
    # Esta es para ver la planilla original completa
    path('blogs',views.blogs, name="Blog"),
    
    path('comment/<id>',views.comment, name="Comment"),
    path('showBlog/<id>',views.showBlog, name="ShowBlog"),

    path("busquedaBlog/",views.busquedaBlog, name ="BusquedaBlog"),
    path("buscar/",views.buscar, name ="Buscar"),

    path('blogForm/',views.blogForm, name="BlogForm"),
    path('tagForm/',views.tagForm, name="TagForm"),
    path('commentForm/',views.commentForm, name="CommentForm"),
]