from django.shortcuts import render
# from django.shortcuts import render
from AppProyecto1.models import Blog, Tag, Comment


def blogs(request):
    blogs=Blog.objects.all()
    return render(request, 'AppProyecto1/blogs.html',{"blogs":blogs})

def comment(request,id):
    comment=Comment.objects.get(id=id)
    return render(request, 'AppProyecto1/comment.html', {"comment":comment})

def showBlog(request,id):
    blog=Blog.objects.get(id=id)
    tags=Tag.objects.filter(blog__id=id)
    return render(request, 'AppProyecto1/showBlog.html', {"blog":blog,"tags":tags})

    # Páginas nuevas agregadas:

def inicio(request):
    # return render(request, 'AppProyecto1/index.html')
    return render(request, 'AppProyecto1/inicio.html')

def padre(request):
    return render(request, 'AppProyecto1/padre.html')

def index(request):
    return render(request, 'AppProyecto1/index (plantilla vacía).html')
