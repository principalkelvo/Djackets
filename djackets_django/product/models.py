from django.db import models
from django.db.models.expressions import F

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    class Meta:
        ordering = ('name',) #order by name
        
    def __str__(self): #change to string
            return self.name
        
    def get_absolute_url(self):
            return f'/{self.slug}/'
        
# Create your models here.
