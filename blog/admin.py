from django.contrib import admin
from .models import Category, Post, Comment # Importamos tus modelos

# Los registramos para que aparezcan en el panel
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)