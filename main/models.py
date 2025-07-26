from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_height=100, unique=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    
    def __str__(self):
        return self.name 


    class Product(models.Model):
        category = models.ForeignKey(Category, related_name= "products",
        on_delete=models.CASCADE)
