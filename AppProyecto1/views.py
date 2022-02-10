# from turtle import title
# importación no ocupada

from django.shortcuts import render, HttpResponse
from AppProyecto1.models import Avatar,Blog, Tag, Comment
from AppProyecto1.forms import BlogForm, TagForm, CommentForm, UserRegisterForm, UserEditForm, AvatarForm
from django.views.generic.edit import UpdateView, CreateView,DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id) #le cargamos al inicio la imagen del avatar del usuario logeado
    tags = Tag.objects.all()
    if avatares:
        return render(request,"AppProyecto1/inicio.html",{"url":avatares[0].imagen.url,"tags":tags})
    else:
        return render(request,"AppProyecto1/inicio.html",{"tags":tags})

def index(request):
    return render(request, 'AppProyecto1/index.html')
# Inicio Integración desde rama_flor_2

def login_request(request):
    tags = Tag.objects.all()
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
                    return render(request,"AppProyecto1/inicio.html",{"mensaje":f"Bienvenido {username}","url":avatares[0].imagen.url,"tags":tags})
                else:
                    return render(request,"AppProyecto1/inicio.html",{"mensaje":f"Bienvenido {username}","tags":tags})
            else:
                return render(request,"AppProyecto1/inicio.html",{"mensaje":"Error, datos incorrectos","tags":tags})
        else:
            return render(request,"AppProyecto1/inicio.html",{"mensaje":"Error, formulario erroneo","tags":tags})
    form = AuthenticationForm()
    return render(request,"AppProyecto1/login.html",{'form':form,"tags":tags})

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
        miFormulario = UserEditForm(initial={'email':user.email,'first_name':user.first_name,'last_name':user.last_name})

    return render(request,"AppProyecto1/editarPerfil.html",{"miFormulario":miFormulario, "user":user})

@login_required
def avatarForm(request):
    if(request.method == "POST"):
        myAvatarForm = AvatarForm(request.POST, request.FILES)

        if myAvatarForm.is_valid():
            user=User.objects.get(username=request.user)
            Avatar.objects.filter(user=user.id).delete()
            avatar=Avatar(user=user, imagen=myAvatarForm.cleaned_data['imagen'])
            avatar.save()
            return render(request,'AppProyecto1/inicio.html',{"url":avatar.imagen.url})
    else:
        myAvatarForm = AvatarForm()
    return render(request,"AppProyecto1/avatarForm.html",{'myAvatarForm':myAvatarForm})

# Fin Integración desde rama_flor_2

class BlogLista(ListView):
    model = Blog
    template_name = "AppProyecto1/blog_lista.html"
    
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class BlogDetalle (DetailView):
    model = Blog
    template_name = "AppProyecto1/blog_detalle.html"

    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super(BlogDetalle, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['blogtags'] = Tag.objects.filter(blog=self.get_object())
        context['blogcomments'] = Comment.objects.filter(blog=self.get_object())
        return context
class BlogCreate (CreateView):
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Blog
    success_url= "/AppProyecto1/blog_lista/"
    fields = ["title","subtitle","body","tag"]

class BlogUpdate(UpdateView):
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"
    fields = ["title","subtitle","body","tag"]
        
class BlogDelete(DeleteView):
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"

# CRUD de tags:
        
class TagLista(ListView):
    model= Tag
    template_name ="AppProyecto1/tag_lista.html"
    
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class TagCreate (CreateView):
    model= Tag
    success_url="/AppProyecto1/tag_lista/"
    fields = ["name"]
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class TagDelete(DeleteView):
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Tag
    success_url ="/AppProyecto1/tag_lista/"

# Integración de definiciones de rama_flor_2

def blogTagLista(request,tag):
    tags = Tag.objects.all()
    blogs = Blog.objects.filter(tag=tag)
    return render(request,"AppProyecto1/blog_lista.html",{'object_list':blogs,"tags":tags})
    

def acercaDe(request):
    tags = Tag.objects.all()
    return render(request,"AppProyecto1/about.html",{"tags":tags})

def commentLista(request, blog):
    tags = Tag.objects.all()
    comments=Comment.objects.filter(blog=blog)
    return render(request,"AppProyecto1/comment_lista.html",{"comments":comments, "blog":blog,"tags":tags})


def commentForm(request, blog):
    tags = Tag.objects.all()
    if(request.method == "POST"):
        commentForm = CommentForm(request.POST)

        if commentForm.is_valid():
            informacion = commentForm.cleaned_data
            blogObj = Blog.objects.get(id=blog)
            comment = Comment(text=informacion['text'], blog=blogObj)
            comment.save()
            comments = Comment.objects.filter(blog=blog)
            return render(request,"AppProyecto1/comment_lista.html",{"comments":comments,"blog":blog,"tags":tags})
    else:
        commentForm=CommentForm()
    return render(request,"AppProyecto1/comment_form.html",{"commentForm":commentForm,"blog":blog,"tags":tags})

class CommentUpdate(UpdateView):
    model = Comment
    success_url = "/AppProyecto1/blog_lista/"
    fields=["text","blog"]
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context


class CommentDelete(DeleteView):
    model = Comment
    success_url = "/AppProyecto1/blog_lista/"
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
