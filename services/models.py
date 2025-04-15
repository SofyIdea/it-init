from django.db import models

# Create your models here.
class Services(models.Model):
    title = models.CharField(max_length = 150)
    about = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return self.title