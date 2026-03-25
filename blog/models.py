from django.db import models
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories" # Así corriges el nombre en el admin
# Create your models here.
