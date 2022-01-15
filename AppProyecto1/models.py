from django.db import models


class Tag(models.Model):
    name=models.CharField(max_length=40)

class Blog(models.Model):
    title=models.CharField(max_length=40)
    subtitle=models.CharField(max_length=40)
    body=models.TextField()
    tags=models.ManyToManyField(Tag)

class Comment(models.Model):
    text=models.TextField()
    Blog=models.ForeignKey(Blog,on_delete=models.CASCADE)