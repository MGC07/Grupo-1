from django.shortcuts import render
from django.shortcuts import render
from AppProyecto1.models import Blog, Tag, Comment


def blogs(request):
    blogs=Blog.objects.all()
    return render(request,'blogs.html',{"blogs":blogs})

def comment(request,id):
    comment=Comment.objects.get(id=id)
    return render(request, 'comment.html', {"comment":comment})

def showBlog(request,id):
    blog=Blog.objects.get(id=id)
    tags=Tag.objects.filter(blog__id=id)
    return render(request, 'showBlog.html', {"blog":blog,"tags":tags})