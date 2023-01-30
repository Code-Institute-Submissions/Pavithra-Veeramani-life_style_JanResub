from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Review(models.Model):
    """
    Model to represent a Product review
    """
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='reviews')
    content = models.TextField(verbose_name="")
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_product_reviews')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"Review {self.content} for {self.product} by {self.created_by}"
