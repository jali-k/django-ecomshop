from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    slug = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photos/categories", blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_url(self):
        return f"/{self.slug}/"

    def __str__(self):
        return self.name
