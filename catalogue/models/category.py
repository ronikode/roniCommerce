"""

"""
from django.db import models
from django.urls import reverse


class CategoryModel(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        db_table = "categoria"
        ordering = ("name",)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('catalogue:item_catalogue_slug', args=[self.slug])
