from django.shortcuts import render, HttpResponse
from AppProyecto1.models import Avatar,Blog, Mensajeria, Tag, Comment
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
    tags = Tag.objects.all()
    if avatares:
        return render(request,"AppProyecto1/inicio.html",{"url":avatares[0].imagen.url,"tags":tags})
    else:
        return render(request,"AppProyecto1/inicio.html",{"tags":tags})

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
    tags = Tag.objects.all()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            informacion = form.cleaned_data
            form.save()
            user = User.objects.get(username=informacion['username'])
            my_group = Group.objects.get(name='Users') 
            my_group.user_set.add(user)
            return render(request,"AppProyecto1/inicio.html",{"mensaje":"Usuario creado","tags":tags})

    else:
        form = UserRegisterForm()
    return render(request,"AppProyecto1/registro.html",{"form":form,"tags":tags})

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
    avatar=Avatar.objects.filter(user=user.id)
    if(request.method == "POST"):
        myAvatarForm = AvatarForm(request.POST, request.FILES)

        if myAvatarForm.is_valid():
            informacion = myAvatarForm.cleaned_data
            if avatar:
                if informacion['imagen']:
                    avatar[0].imagen=informacion['imagen']
                avatar[0].descripcion=informacion['descripcion']
                avatar[0].link=informacion['link']
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
        if avatar:
            myAvatarForm = AvatarForm(
                initial={
                    'descripcion':avatar[0].descripcion,
                    'link':avatar[0].link
                    })
        else:
            myAvatarForm = AvatarForm()
    return render(request,"AppProyecto1/avatarForm.html",{'myAvatarForm':myAvatarForm})

# Fin Integración desde rama_flor_2

@method_decorator(login_required, name='dispatch')
class BlogLista(ListView):
    model = Blog
    template_name = "AppProyecto1/blog_lista.html"
    
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

class BlogBusqueda(ListView):
    model = Blog
    template_name = "AppProyecto1/blog_lista.html"

    def get_queryset(self):
        result = super(BlogBusqueda, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Blog.objects.filter(title__contains=query)
            result = postresult
        else:
            result = None
        return result
    
    def get_context_data(self,**kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class BlogDetalle (DetailView):
    model = Blog
    template_name = "AppProyecto1/blog_detalle.html"
    def get_context_data(self,**kwargs): # Función para invocar tags
        context = super(BlogDetalle,self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        context['blogtags'] = Tag.objects.filter(blog=self.get_object())
        context['blogcomments'] = Comment.objects.filter(blog=self.get_object())
        return context

@method_decorator(login_required, name='dispatch')
class BlogCreate (CreateView):
    def get_context_data(self,**kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Blog
    success_url= "/AppProyecto1/blog_lista/"
    fields = ["title","subtitle","body","tag","imagen"]

    def form_valid(self, form):
        form.instance.autor=self.request.user
        return super(BlogCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BlogUpdate(UpdateView):
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"
    fields = ["title","subtitle","body","tag","imagen","fechaCreacion","publicacion"]
        
@method_decorator(login_required, name='dispatch')   
class BlogDelete(DeleteView):
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Blog
    success_url = "/AppProyecto1/blog_lista/"

@method_decorator(login_required, name='dispatch')       
class TagLista(ListView):
    model= Tag
    template_name ="AppProyecto1/tag_lista.html"
    
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

@login_required
def blogTagLista(request,tag):
    blogs = Blog.objects.filter(tag=tag)
    return render(request,"AppProyecto1/blog_lista.html",{'object_list':blogs})

@method_decorator(login_required, name='dispatch')
class TagCreate (CreateView):
    model= Tag
    success_url="/AppProyecto1/tag_lista/"
    fields = ["name"]
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

@method_decorator(login_required, name='dispatch')
class TagDelete(DeleteView):
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    model= Tag
    success_url ="/AppProyecto1/tag_lista/"

@login_required
def blogTagLista(request,tag):
    tags = Tag.objects.all()
    blogs = Blog.objects.filter(tag=tag)
    return render(request,"AppProyecto1/blog_lista.html",{'object_list':blogs,"tags":tags})
    

def acercaDe(request):
    tags = Tag.objects.all()
    return render(request,"AppProyecto1/about.html",{"tags":tags})

# Este ya no se ocupa
# def commentLista(request, blog):
    # tags = Tag.objects.all()
    # comments=Comment.objects.filter(blog=blog)
    # return render(request,"AppProyecto1/comment_lista.html",{"comments":comments, "blog":blog,"tags":tags})

@login_required
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
            blogtags = Tag.objects.filter(blog=blog)
            return render(request,"AppProyecto1/blog_detalle.html",{"blogcomments":comments,"blog":blogObj,"tags":tags,"blogtags":blogtags})
    else:
        commentForm=CommentForm()
    return render(request,"AppProyecto1/comment_form.html",{"commentForm":commentForm,"blog":blog,"tags":tags})

@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    model = Comment
    success_url = "/AppProyecto1/blog_lista/"
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

@login_required
def inboxview(request):
    inbox = Mensajeria.objects.filter(receptor=request.user)
    enviados = Mensajeria.objects.filter(remitente=request.user)
    tags = Tag.objects.all()
    return render(request,"AppProyecto1/mensajes_lista.html",{"inbox":inbox,"tags":tags,"enviados":enviados})

@method_decorator(login_required, name='dispatch')
class MensajeCreate (CreateView):
    model= Mensajeria
    success_url="/AppProyecto1/inbox/"
    fields = ["receptor","contenido"]

    def form_valid(self, form):
        form.instance.remitente = self.request.user
        return super(MensajeCreate, self).form_valid(form)

    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context
    


@method_decorator(login_required, name='dispatch')
class MensajeDelete(DeleteView):
    model = Mensajeria
    success_url = "/AppProyecto1/inbox/"
    def get_context_data(self, **kwargs): # Función para invocar tags
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context