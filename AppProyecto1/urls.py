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

    path("blog_lista/",views.BlogLista.as_view(), name= 'List'),
    path("detalle/<pk>/",views.BlogDetalle.as_view(), name= 'Detail'),
    path("nuevo/",views.BlogCreate.as_view(), name= 'New'),
    path("editar/<pk>/",views.BlogUpdate.as_view(), name= 'Edit'),
    path("borrar/<pk>/",views.BlogDelet.as_view(), name= 'Delete'),

    path("tag_lista/",views.TagLista.as_view(), name= 'Listt'),
    path("detalle_tag/<pk>/",views.TagDetalle.as_view(), name= 'Detailt'),
    path("nuevo_tag/",views.TagCreate.as_view(), name= 'Newt'),
    path("editar_tag/<pk>/",views.TagUpdate.as_view(), name= 'Editt'),
    path("borrar_tag/<pk>/",views.TagDelet.as_view(), name= 'Deletet'),

     
    path('comment_lista/', views.CommentLista.as_view(), name = 'Listc'),
    path('detalle/<pk>/', views.CommentDetalle.as_view(), name = 'Detailc'),
    path('nuevo/', views.CommentCreate.as_view(), name = 'Newc'),
    path('editar/<pk>/', views.CommentUpdate.as_view(), name = 'Editc'),
    path('borrar/<pk>/', views.CommentDelet.as_view(), name = 'Deletec'),
    

]