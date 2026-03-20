from django.db import models

class Category(models.Model):
    # Error corregido: max_length (con 'th' al final)
    title = models.CharField(max_length=225) 
    
    class Meta:
        # Error corregido: agregada coma para que sea tupla válida
        ordering = ('title',) 
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    # Cambiado a lista de tuplas para mejor compatibilidad
    CHOICES_STATUS = [
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    ]        

    category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=225)
    intro = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Cambiado a status (minúscula por convención)
    status = models.CharField(max_length=10, choices=CHOICES_STATUS, default=ACTIVE)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return self.title
   
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=225)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name