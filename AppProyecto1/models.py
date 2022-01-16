from django.db import models


class Tag(models.Model):
    name=models.CharField(max_length=40)

class Blog(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=models.TextField()
    tag=models.ManyToManyField(Tag) #Este many to many crea la tabla blog_tag en la base

class Comment(models.Model):
    text=models.TextField()
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)