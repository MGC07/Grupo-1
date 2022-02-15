#### Grupo 1

##### Proyecto

Generar la estrucutura de un Blog utilizando lo aprendido en clase a traves de la herraminta de Django

##### Estado del proyecto

En desarrollo, en esta primer etapa se encuentra desarrollado los siguientes conceptos:
Herencia
Modelos
Formularios
Buscar en un Formulario

##### Requisitos del entorno

Para poder replicar el proyecto debera tener instalado Python /Django y tener acceso a Github
Para mas etalle como instalar las mismas, se dejan los siguientes links
<https://www.python.org>
<https://www.djangoproject.com>
<https://github.com>
Para descargar el proyecto debera clonar el mismo ingresando el siguiente comando
git clone <https://github.com/MGC07/Grupo-1.git>

#### Informacion sobre el desarrollo

##### Equipo de trabajo

Se dividio el trabajo sobre los temas que mas nos sentiamos seguros en desarrollar, creamos diferentes ramas para trabajar en paralelo.

Maria Florencia Mendoza-- login/logout, register, Perfiles, Avatar, grupos Admin y Usuarios, permisos.

Martin Bonnefoy Valdés -- Herencias HTML, aspectos visuales, implementación de navbar y sidebar, sistemas de búsqueda (cuadro de búsqueda y según tags), sistema de mensajería.

Maria Guadalupe Casas --Alta Github , buscar en formularios, crear en el modelo de blog Fecha de Creacion/fecha de Publicacion/Autor, chekeditor, unit-test  y Readme

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
