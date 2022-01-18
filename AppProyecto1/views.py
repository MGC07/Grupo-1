from turtle import title
from django.shortcuts import render, HttpResponse
from AppProyecto1.models import Blog, Tag, Comment
from AppProyecto1.forms import BlogForm, TagForm, CommentForm

def inicio(request):
    return render(request, 'AppProyecto1/inicio.html')

def padre(request):
    return render(request, 'AppProyecto1/padre.html')

def index(request):
    return render(request, 'AppProyecto1/index (plantilla vacía).html')

# def blogs(request):
#     blogs=Blog.objects.all()
#     return render(request, 'AppProyecto1/blogs.html', {"blogs":blogs})

def blogs(request):
    blogs=Blog.objects.all()
    return render(request, 'AppProyecto1/blogs.html',{"blogs":blogs})

def comment(request,id):    #django se aviva que el <id> del url tiene que venir como parametro
    comment=Comment.objects.get(id=id)  #id de la izquierda es el de la base, id de la derecha es el del url
    return render(request, 'AppProyecto1/comment.html', {"comment":comment})

def showBlog(request,id):
    blog=Blog.objects.get(id=id)    #El get devuelve un solo elemento.
    tags=Tag.objects.filter(blog__id=id)    #Aca django se aviva de que tiene que buscar en la tabla blog_tag y te devuelve todos los tags que estan relacionados con ese blog__id
                                            #El filter devuelve todos los elementos que cumplen la condicion blog__id = id
    comment= Comment.objects.filter(blog=blog)
    return render(request, 'AppProyecto1/showBlog.html', {"blog":blog,"tags":tags,"comment":comment})

def busquedaBlog(request):
    return render(request, "AppProyecto1/busquedaBlog.html")
    
def buscar (request):
    if request.GET["titulo"]:
            titulo = request.GET["titulo"] 
            blogs= Blog.objects.filter(title=titulo)
            return render(request,"AppProyecto1/busqueda.html", {"titulo":titulo,"blogs":blogs})
    else:
            respuesta= "No enviaste Datos"
    return HttpResponse(respuesta) 
    

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
            return render(request,'AppProyecto1/blogs.html',{"blogs":blogs})
    else:
        myBlogForm = BlogForm()
    return render(request,"AppProyecto1/blogForm.html",{'myBlogForm':myBlogForm})

def tagForm(request):
    if(request.method == "POST"):
        myTagForm = TagForm(request.POST)

        if myTagForm.is_valid():
            info = myTagForm.cleaned_data
            tag = Tag(name=info['name'])
            tag.save()
            blogs=Blog.objects.all()
            return render(request,'AppProyecto1/blogs.html',{"blogs":blogs})
    else:
        myTagForm = TagForm()
    return render(request,"AppProyecto1/tagForm.html",{'myTagForm':myTagForm})


def commentForm(request):
    if(request.method == "POST"):
        myCommentForm = CommentForm(request.POST)

        if myCommentForm.is_valid():
            info = myCommentForm.cleaned_data
            comment = Comment(text=info['text'], blog=info['blog'])
            comment.save()
            return render(request,'AppProyecto1/comment.html',{"comment":comment})
    else:
        myCommentForm = CommentForm() #instancia de formulario
    return render(request,"AppProyecto1/commentForm.html",{'myCommentForm':myCommentForm})
