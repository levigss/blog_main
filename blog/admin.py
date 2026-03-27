from django.contrib import admin
from .models import Category, Post, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',) # Cambia 'title' por 'name' (que es el que tiene tu modelo)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # Solo ponemos los campos que existen en tu models.py: title, content, category
    list_display = ('title', 'category') 
    # Quitamos 'created_at' y 'status' porque no existen en tu modelo actual

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Cambia 'name' por 'author' (que es el campo que definimos para el comentario)
    list_display = ('author', 'post', 'created_at')