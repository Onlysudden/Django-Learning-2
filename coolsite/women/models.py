from django.db import models
from django.urls import reverse

class Women(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото') # Создается удобная директория под фото
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания') # Создается один раз и не меняется
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время обновления') # Меняется каждый раз при изменении
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    cat = models.ForeignKey("Category", on_delete=models.PROTECT, null=True, verbose_name='Категория') # Category пишем как строку, либо как переменную, но тогда Category должна быть перед Women

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Известные женщины"
        verbose_name_plural = "Известные женщины"
        ordering = ['time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ['id']
