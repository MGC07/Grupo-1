from turtle import title
from django.shortcuts import render, HttpResponse
from AppProyecto1.models import Blog, Tag, Comment,
from AppProyecto1.forms import BlogForm, TagForm, CommentForm
from django.views.generic.edit import UpdateView, CreateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView


def inicio(request):
    return render(request, 'AppProyecto1/inicio.html')

def padre(request):
    return render(request, 'AppProyecto1/padre.html')

def index(request):
    return render(request, 'AppProyecto1/index (plantilla vacía).html')


def blogs(request):
    blogs=Blog.objects.all()
    return render(request, 'AppProyecto1/blogs.html',{"blogs":blogs})

def comment(request,id):    #django se aviva que el <id> del url tiene que venir como parametro
    comment=Comment.objects.get(id=id)  #id de la izquierda es el de la base, id de la derecha es el del url
    return render(request, 'AppProyecto1/showBlog.html', {"blog": blog, "tags": tags,"comments":comments})

def showBlog(request,id):
    blog=Blog.objects.get(id=id)    #El get devuelve un solo elemento.
    tags=Tag.objects.filter(blog__id=id)    #Aca django se aviva de que tiene que buscar en la tabla blog_tag y te devuelve todos los tags que estan relacionados con ese blog__id
                                            #El filter devuelve todos los elementos que cumplen la condicion blog__id = id
    comments=Comment.objects.filter(blog__id=id)
    return render(request, 'AppProyecto1/showBlog.html', {"blog":blog,"tags":tags,"comments":comments})

def busquedaBlog(request):
    return render(request, "AppProyecto1/busquedaBlog.html")
    
def buscar (request):
    if request.GET["titulo"]:
            titulo = request.GET["titulo"] 
            blogs= Blog.objects.filter(title__icontains=titulo) # Se modifica para buscar resultados "que contengan a"
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
            return render(request,'AppProyecto1/inicio.html')
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
            return render(request,'AppProyecto1/inicio.html')
    else:
        myCommentForm = CommentForm() #instancia de formulario
    return render(request,"AppProyecto1/commentForm.html",{'myCommentForm':myCommentForm})

class BlogLista(ListView):
    model = Blog
    template_name = "AppProyecto1/blog_lista.html"

class BlogDetalle (DetailView):
    model = Blog
    template_name = "AppProyecto1/blog_detalle.html"

class BlogCreate (CreateView):
    model= Blog
    success_url= "/AppProyecto1/blog_form/"
    fields = ["title","subtitle","body","tag"]

class  BlogUpdate(UpdateView):
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"
    fields = ["title","subtitle","body","tag"]
        
class BlogDelet(DeleteView):
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"


        
class TagLista(ListView):
    model= Tag
    template_name ="AppProyecto1/tag_lista.html"

class TagDetalle (DetailView):
    model = Tag
    template_name ="AppProyecto1/tag_detalle.html"

class TagCreate (CreateView):
    model= Tag
    success_url="/AppProyecto1/tag_form/"
    fields = ["name"]

class  TagUpdate(UpdateView):
    model= Tag
    success_url ="/AppProyecto1/tag_lista/"
    fields = ["name"]
        
class TagDelet(DeleteView):
    model= Tag
    success_url ="/AppProyecto1/tag_lista/"


class CommentLista(ListView):
    model = Comment
    template_name = "AppProyecto1/comment_lista.html"

class CommentDetalle(DetailView):
    model = Comment
    template_name ="AppProyecto1/comment_detalle.html"


class CommentCreate(CreateView):
    model = Comment
    success_url = "/AppProyecto1/comment_form.html/"
    fields=["text","blog"]


class CommentUpdate(UpdateView):
    model = Comment
    success_url = "/AppProyecto1/comment_lista/"
    fields=["text","blog"]


class CommentDelet(DeleteView):
    model = Comment
    success_url = "/AppProyecto1/comment_lista/"