from django.db import models

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class NewsMedia(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='media')
    media = models.FileField(upload_to='news/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.news.title