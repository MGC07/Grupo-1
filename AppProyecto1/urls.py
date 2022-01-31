from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AppProyecto1 import views
from django.contrib.auth.views import LogoutView

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

    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppProyecto1/logout.html'), name='Logout'),

    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('avatarForm/', views.avatarForm, name="AvatarForm"),
]