from django import forms
from AppProyecto1.models import Mensajeria, Tag, Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class BlogForm(forms.Form):
    title=forms.CharField(max_length=40)
    subtitle=forms.CharField(max_length=40)
    body=forms.CharField(widget=forms.Textarea)
    tags=forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),widget=forms.CheckboxSelectMultiple)
    imagen=forms.ImageField()
    fechaCreacion= forms.DateTimeField()
    publicacion= forms.DateTimeField()  
    
  

class TagForm(forms.Form):
    name=forms.CharField(max_length=40)

class CommentForm(forms.Form):
    text=forms.CharField(widget=forms.Textarea)

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Modificar Email")
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(required=False)
    descripcion = forms.CharField(widget=forms.Textarea)
    link = forms.URLField()

class MensajeForm(forms.ModelForm):
    receptor=forms.CharField(max_length=40)
    contenido=forms.CharField(widget=forms.Textarea)
    created_at = forms.DateTimeField()
    class Meta:
        model = Mensajeria
        exclude = ['remitente']