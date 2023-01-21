from django.db import models
from django.contrib.auth.models import User
from products.model import Product

# Create your models here.
class Review(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Review {self.product} by {self.name}"