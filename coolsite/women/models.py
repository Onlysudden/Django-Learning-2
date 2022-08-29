from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/") # Создается удобная директория под фото
    time_create = models.DateTimeField(auto_now_add=True) # Создается один раз и не меняется
    time_update = models.DateTimeField(auto_now=True) # Меняется каждый раз при изменении
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True) # Category пишем как строку, либо как переменную, но тогда Category должна быть перед Women

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
