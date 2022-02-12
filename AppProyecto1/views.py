from django.shortcuts import render, HttpResponse
from AppProyecto1.models import Avatar,Blog, Tag, Comment
from AppProyecto1.forms import BlogForm, TagForm, CommentForm, UserRegisterForm, UserEditForm, AvatarForm
from django.views.generic.edit import UpdateView, CreateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id) #le cargamos al inicio la imagen del avatar del usuario logeado
    if avatares:
        return render(request,"AppProyecto1/inicio.html",{"url":avatares[0].imagen.url})
    else:
        return render(request,"AppProyecto1/inicio.html")
# Inicio Integración desde rama_flor_2

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
                if avatares:
                    return render(request,"AppProyecto1/inicio.html",{"mensaje":f"Bienvenido {username}","url":avatares[0].imagen.url})
                else:
                    return render(request,"AppProyecto1/inicio.html",{"mensaje":f"Bienvenido {username}"})
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
            informacion = form.cleaned_data
            form.save()
            user = User.objects.get(username=informacion['username'])
            my_group = Group.objects.get(name='Users') 
            my_group.user_set.add(user)
            return render(request,"AppProyecto1/inicio.html",{"mensaje":"Usuario creado"})

    else:
        form = UserRegisterForm()
    return render(request,"AppProyecto1/registro.html",{"form":form})

@login_required
def verPerfil(request):
    user = request.user
    avatar = Avatar.objects.filter(user=user.id)
    if avatar:
        return render(request,"AppProyecto1/verPerfil.html",{"user":user, "avatar":avatar[0]})
    else:
        return render(request,"AppProyecto1/verPerfil.html",{"user":user})

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
            avatar = Avatar.objects.filter(user=user.id)
            if avatar:
                return render(request,"AppProyecto1/verPerfil.html",{"user":user, "avatar":avatar[0]})
            else:
                return render(request,"AppProyecto1/verPerfil.html",{"user":user})

    else:
        miFormulario = UserEditForm(
            initial={
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name
                })

    return render(request,"AppProyecto1/editarPerfil.html",{"miFormulario":miFormulario, "user":user})

@login_required
def avatarForm(request):
    user=User.objects.get(username=request.user)
    avatar=Avatar.objects.filter(user=user.id)[0]
    if(request.method == "POST"):
        myAvatarForm = AvatarForm(request.POST, request.FILES)

        if myAvatarForm.is_valid():
            informacion = myAvatarForm.cleaned_data
            if avatar:
                if informacion['imagen']:
                    avatar.imagen=informacion['imagen']
                avatar.descripcion=informacion['descripcion']
                avatar.link=informacion['link']
            else:
                avatar=Avatar(
                    user=user,
                    imagen=informacion['imagen'],
                    descripcion=informacion['descripcion'],
                    link=informacion['link']
                    )
            avatar.save()
            return render(request,"AppProyecto1/verPerfil.html",{"user":user, "avatar":avatar})
    else:
        myAvatarForm = AvatarForm(
            initial={
                'descripcion':avatar.descripcion,
                'link':avatar.link
                })
    return render(request,"AppProyecto1/avatarForm.html",{'myAvatarForm':myAvatarForm})

# Fin Integración desde rama_flor_2

@method_decorator(login_required, name='dispatch')
class BlogLista(ListView):
    model = Blog
    template_name = "AppProyecto1/blog_lista.html"

@method_decorator(login_required, name='dispatch')
class BlogDetalle (DetailView):
    model = Blog
    template_name = "AppProyecto1/blog_detalle.html"

@method_decorator(login_required, name='dispatch')
class BlogCreate (CreateView):
    model= Blog
    success_url= "/AppProyecto1/blog_lista/"
    fields = ["title","subtitle","body","tag"]

@method_decorator(login_required, name='dispatch')
class BlogUpdate(UpdateView):
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"
    fields = ["title","subtitle","body","tag"]

@method_decorator(login_required, name='dispatch')        
class BlogDelete(DeleteView):
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"

@method_decorator(login_required, name='dispatch')       
class TagLista(ListView):
    model= Tag
    template_name ="AppProyecto1/tag_lista.html"

@login_required
def blogTagLista(request,tag):
    blogs = Blog.objects.filter(tag=tag)
    return render(request,"AppProyecto1/blog_lista.html",{'object_list':blogs})

@method_decorator(login_required, name='dispatch')
class TagCreate (CreateView):
    model= Tag
    success_url="/AppProyecto1/tag_form/"
    fields = ["name"]

@method_decorator(login_required, name='dispatch')
class TagDelete(DeleteView):
    model= Tag
    success_url ="/AppProyecto1/tag_lista/"

@login_required
def commentLista(request, blog):
    comments=Comment.objects.filter(blog=blog)
    return render(request,"AppProyecto1/comment_lista.html",{"comments":comments, "blog":blog})

@login_required
def commentForm(request, blog):
    if(request.method == "POST"):
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            informacion = commentForm.cleaned_data
            blogObj = Blog.objects.get(id=blog)
            comment = Comment(text=informacion['text'], blog=blogObj)
            comment.save()
            comments = Comment.objects.filter(blog=blog)
            return render(request,"AppProyecto1/comment_lista.html",{"comments":comments,"blog":blog})
    else:
        commentForm=CommentForm()
    return render(request,"AppProyecto1/comment_form.html",{"commentForm":commentForm,"blog":blog})

@method_decorator(login_required, name='dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    success_url = "/AppProyecto1/blog_lista/"
    fields=["text","blog"]

@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    model = Comment
    success_url = "/AppProyecto1/blog_lista/"
