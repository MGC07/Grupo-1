import django.views.defaults
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AppProyecto1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio,name="Inicio"),

    path( 'about/', views.acercaDe, name="About"),
    path("blog_lista/",views.BlogLista.as_view(), name= 'BlogList'),
    path("blog_busqueda/",views.BlogBusqueda.as_view(), name= 'BlogSearch'),
    path("detalle/<pk>/",views.BlogDetalle.as_view(), name= 'BlogDetail'),
    path("blog_nuevo/",views.BlogCreate.as_view(), name= 'BlogNew'),
    path("blog_editar/<pk>/",views.BlogUpdate.as_view(), name= 'BlogEdit'),
    path("blog_borrar/<pk>/",views.BlogDelete.as_view(), name= 'BlogDelete'),
    path("tag_lista/",views.TagLista.as_view(), name= 'TagList'),
    path("blogTagLista/<tag>", views.blogTagLista, name= 'BlogTagLista'),

    path("nuevo_tag/",views.TagCreate.as_view(), name= 'TagNew'),
    path("borrar_tag/<pk>/",views.TagDelete.as_view(), name= 'TagDelete'),

    # path('comment_lista/<blog>', views.commentLista, name = 'CommentList'),
    path('comment_nuevo/<blog>', views.commentForm, name = 'CommentNew'),
    path('comment_borrar/<pk>/', views.CommentDelete.as_view(), name = 'CommentDelete'),

    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppProyecto1/logout.html'), name='Logout'),
    path('verPerfil/', views.verPerfil, name="VerPerfil"),
    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('avatarForm/', views.avatarForm, name="AvatarForm"),
    
    path('redactar/', views.MensajeCreate.as_view(), name = 'RedactarMensaje'),
    path('inbox/', views.inboxview, name = 'Inbox'),
    path('eliminarmensaje/<pk>/', views.MensajeDelete.as_view(), name = 'EliminarMensaje'),

]