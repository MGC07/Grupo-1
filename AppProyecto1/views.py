from django.shortcuts import render, HttpResponse
from AppProyecto1.models import Avatar, Blog, Tag, Comment
from AppProyecto1.forms import BlogForm, TagForm, CommentForm, UserRegisterForm, UserEditForm, AvatarForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required
def inicio(request):

    avatares = Avatar.objects.filter(user=request.user.id) #le cargamos al inicio la imagen del avatar del usuario logeado

    return render(request, 'AppProyecto1/inicio.html', {"url":avatares[0].imagen.url})

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

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render(request,"AppProyecto1/inicio.html",{"mensaje":f"Bienvenido {username}","url":avatares[0].imagen.url})
            else:
                return render(request,"AppProyecto1/inicio.html",{"mensaje":"Error, datos incorrectos"})
        else:
            return render(request,"AppProyecto1/inicio.html",{"mensaje":"Error, formulario erroneo"})
    form = AuthenticationForm()
    return render(request,"AppProyecto1/login.html",{'form':form})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            return render(request,"AppProyecto1/inicio.html",{"mensaje":"Usuario creado"})

    else:
        form = UserRegisterForm()
    return render(request,"AppProyecto1/registro.html",{"form":form})

@login_required
def editarPerfil(request):
    user = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            user.email = informacion['email']
            user.password1 = informacion['password1']
            user.password2 = informacion['password2']
            user.first_name = informacion['first_name']
            user.last_name = informacion['last_name']
            user.save()
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request,"AppProyecto1/inicio.html",{"url":avatares[0].imagen.url})

    else:
        miFormulario = UserEditForm(initial={'email':user.email})

    return render(request,"AppProyecto1/editarPerfil.html",{"miFormulario":miFormulario, "user":user})

@login_required
def avatarForm(request):
    if(request.method == "POST"):
        myAvatarForm = AvatarForm(request.POST, request.FILES)

        if myAvatarForm.is_valid():
            user=User.objects.get(username=request.user)
            avatar=Avatar(user=user, imagen=myAvatarForm.cleaned_data['imagen'])
            avatar.save()
            return render(request,'AppProyecto1/inicio.html',{"url":avatar.imagen.url})
    else:
        myAvatarForm = AvatarForm()
    return render(request,"AppProyecto1/avatarForm.html",{'myAvatarForm':myAvatarForm})