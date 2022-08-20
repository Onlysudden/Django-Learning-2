from django.db import models

class Women(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/") # Создается удобная директория под фото
    time_create = models.DateTimeField(auto_now_add=True) # Создается один раз и не меняется
    time_update = models.DateTimeField(auto_now=True) # Меняется каждый раз при изменении
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title
