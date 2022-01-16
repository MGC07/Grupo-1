from turtle import title
from django.shortcuts import render
from django.shortcuts import render
from AppProyecto1.models import Blog, Tag, Comment
from AppProyecto1.forms import BlogForm, TagForm, CommentForm


def blogs(request):
    blogs=Blog.objects.all()
    return render(request,'blogs.html',{"blogs":blogs})

def comment(request,id):    #django se aviva que el <id> del url tiene que venir como parametro
    comment=Comment.objects.get(id=id)  #id de la izquierda es el de la base, id de la derecha es el del url
    return render(request, 'comment.html', {"comment":comment})

def showBlog(request,id):
    blog=Blog.objects.get(id=id)    #El get devuelve un solo elemento.
    tags=Tag.objects.filter(blog__id=id)    #Aca django se aviva de que tiene que buscar en la tabla blog_tag y te devuelve todos los tags que estan relacionados con ese blog__id
                                            #El filter devuelve todos los elementos que cumplen la condicion blog__id = id
    return render(request, 'showBlog.html', {"blog":blog,"tags":tags})

def blogForm(request):
    if(request.method == "POST"):
        myBlogForm = BlogForm(request.POST)

        if myBlogForm.is_valid():
            info = myBlogForm.cleaned_data
            blog = Blog(title=info['title'],subtitle=info['subtitle'],body=info['body'])
            blog.save()
            tags = info['tags']

            for tag in tags:
                blog.tag.add(tag)
            blogs=Blog.objects.all()
            return render(request,'blogs.html',{"blogs":blogs})
    else:
        myBlogForm = BlogForm()
    return render(request,"blogForm.html",{'myBlogForm':myBlogForm})

def tagForm(request):
    if(request.method == "POST"):
        myTagForm = TagForm(request.POST)

        if myTagForm.is_valid():
            info = myTagForm.cleaned_data
            tag = Tag(name=info['name'])
            tag.save()
            blogs=Blog.objects.all()
            return render(request,'blogs.html',{"blogs":blogs})
    else:
        myTagForm = TagForm()
    return render(request,"tagForm.html",{'myTagForm':myTagForm})


def commentForm(request):
    if(request.method == "POST"):
        myCommentForm = CommentForm(request.POST)

        if myCommentForm.is_valid():
            info = myCommentForm.cleaned_data
            comment = Comment(text=info['text'], blog=info['blog'])
            comment.save()
            return render(request,'comment.html',{"comment":comment})
    else:
        myCommentForm = CommentForm() #instancia de formulario
    return render(request,"commentForm.html",{'myCommentForm':myCommentForm})