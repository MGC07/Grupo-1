from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AppProyecto1 import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('index/',views.index, name='Index'), # Esta es para ver la planilla original completa
    path( 'about/', views.acercaDe, name="About"),
    path("blog_lista/",views.BlogLista.as_view(), name= 'BlogList'),
    path("detalle/<pk>/",views.BlogDetalle.as_view(), name= 'BlogDetail'),
    path("blog_nuevo/",views.BlogCreate.as_view(), name= 'BlogNew'),
    path("blog_editar/<pk>/",views.BlogUpdate.as_view(), name= 'BlogEdit'),
    path("blog_borrar/<pk>/",views.BlogDelete.as_view(), name= 'BlogDelete'),

    path("tag_lista/",views.TagLista.as_view(), name= 'TagList'),
    path("nuevo_tag/",views.TagCreate.as_view(), name= 'TagNew'),
    path("borrar_tag/<pk>/",views.TagDelete.as_view(), name= 'TagDelete'),

    path('comment_lista/<blog>', views.commentLista, name = 'CommentList'),
    path('comment_nuevo/<blog>', views.commentForm, name = 'CommentNew'),
    path('comment_editar/<pk>/', views.CommentUpdate.as_view(), name = 'CommentEdit'),
    path('comment_borrar/<pk>/', views.CommentDelete.as_view(), name = 'CommentDelete'),

    path('login/', views.login_request, name='Login'),
    path('register/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppProyecto1/logout.html'), name='Logout'),

    path('editarPerfil/', views.editarPerfil, name="EditarPerfil"),
    path('avatarForm/', views.avatarForm, name="AvatarForm"),
]