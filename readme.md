#### Grupo 1

##### Proyecto

Generar la estrucutura de un Blog utilizando lo aprendido en clase a traves de la herraminta de Django.

##### Estado del proyecto

Finalizado en su primera etapa, en la que se desarrollaron los siguientes conceptos:

Herencia HTML

Modelos

Formularios

Búsqueda por formulario

Sistema de mensajería

Edición de texto avanzada con CKEditor


##### Requisitos del entorno

Para poder replicar el proyecto debera tener instalado:

Python 3.9.5

Django 4.0

django-CKeditor

Pillow

Tener acceso a Github

Para mas detalle como instalar las mismas, se dejan los siguientes links


<https://www.python.org>

<https://www.djangoproject.com>

<https://github.com>


Para descargar el proyecto debera clonar el mismo ingresando el siguiente comando

```
git clone <https://github.com/MGC07/Grupo-1.git>
pip install django=4.0
pip install django-ckeditor
pip install pillow
```

##### Ejecución del proyecto

Para ejecutar el proyecto, es necesario realizar los siguientes comandos:

```
python manage.py migrate
python manage.py loaddata grupo.json
python manage.py createsuperuser
python manage.py runserver
```
_Importante: Para el correcto funcionamiento del proyecto, es necesario realizar dos pasos iniciales con el superuser creado:

(1) En el panel de administración de django es necesario asignar al superuser al grupo Admin

(2) El modelo Blog necesita de la existencia de una instancia del modelo Tag para funcionar, por lo que se hace necesario que un superuser genere una primera etiqueta (Tag) a través del panel de administración de django o del formulario de la página._

Un video que da cuenta de las distintas partes del funcionamiento de la página está disponible en [este link](https://drive.google.com/file/d/1JwGMh3I2OV3Akif0GS9iqV8_JWf0S3cq/view).


#### Informacion sobre el desarrollo

##### Equipo de trabajo

Se dividio el trabajo sobre los temas que mas nos sentiamos seguros en desarrollar, creamos diferentes ramas para trabajar en paralelo.

Maria Florencia Mendoza-- login/logout, register, Perfiles, Avatar, grupos Admin y Usuarios, permisos.

Martin Bonnefoy Valdés -- Herencias HTML, aspectos visuales, implementación de navbar y sidebar, sistemas de búsqueda (cuadro de búsqueda y según tags), sistema de mensajería.

Maria Guadalupe Casas --Alta Github , buscar en formularios, CRUD utilizando vistas basadas en clases, crear en el modelo de blog Fecha de Creacion/fecha de Publicacion/Autor, chekeditor, unit-test  y Readme

##### Informacion de los contenidos dentro de las URLS

1. path('',views.inicio,name="Inicio")# Pagina de Inicio

2. path('padre',views.padre, name="padre")# Esta es para ver la página padre

3. path('index',views.index, name="index")# Esta es para ver la planilla original completa

4. path('blogs',views.blogs, name="Blog")# Muestra los Blogs Disponibles

5. path('comment/<id>',views.comment, name="Comment")# Desde aqui el usuario puede ingresar un comentario al blog elegido

6. path('showBlog/<id>',views.showBlog,name="ShowBlog")# Llama al Blog

7. path("busquedaBlog/",views.busquedaBlog,name ="BusquedaBlog")# Se utiliza para buscar un blog en particular

8. path("buscar/",views.buscar, name ="Buscar")# Formulario de Busqueda

9. path('blogForm/',views.blogForm, name="BlogForm")# Formulario para escribir un Blog

10. path('tagForm/',views.tagForm, name="TagForm")# Formulario para crear tags

11. path('commentForm/',views.commentForm,name="CommentForm")# Formulario para Contacto
  
12. path('inbox/', views.inboxview, name = 'Inbox')# Sistema de mensajería.
