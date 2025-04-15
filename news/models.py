from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 150)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.title