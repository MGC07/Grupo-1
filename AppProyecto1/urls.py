from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from AppProyecto1 import views

urlpatterns = [
    path('blogs/',views.blogs, name='Blog'),
    path('comment/<id>',views.comment, name='Comment'),
    path('showBlog/<id>',views.showBlog, name='ShowBlog'),
    path('blogForm/',views.blogForm, name='BlogForm'),
    path('tagForm/',views.tagForm, name='TagForm'),
    path('commentForm/',views.commentForm, name='CommentForm'),
]