
from django.contrib import admin
from .models import Post, Category, Comment

# 1. Inline para comentarios dentro de un Post
class CommentItemInline(admin.TabularInline):
    model = Comment
    raw_id_fields = ['post']

# 2. Configuración de Post
class PostAdmin(admin.ModelAdmin):
    # Solo dejamos 'title' porque es el único que sabemos que existe
    list_display = ('title',) 
    inlines = [CommentItemInline]

# 3. Configuración de Category
class CategoryAdmin(admin.ModelAdmin):
    # ERROR CORREGIDO: Se agregó la coma final para que sea una tupla
    list_display = ('name',) 
    # Cambié 'title' por 'name' porque las categorías suelen llevar 'name'
    search_fields = ['name'] 

# 4. Configuración de Comment
class CommentAdmin(admin.ModelAdmin):
    # ERROR CORREGIDO: Si no tienes 'name' o 'created_at' en el modelo, fallará.
    # Por ahora dejamos solo 'post' para que te deje avanzar.
    list_display = ('post',) 

# Registro de modelos
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
