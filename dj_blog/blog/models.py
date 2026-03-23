from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    # ... resto de campos ...

class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) # ¿Se llama así?
    created_at = models.DateTimeField(auto_now_add=True)            # ¿O se llama 'fecha'?
    status = models.IntegerField(default=0)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # ... resto de campos ...