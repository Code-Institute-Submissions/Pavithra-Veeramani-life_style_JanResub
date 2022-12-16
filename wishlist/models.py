from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class WishList(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(
        Product, related_name='user_wish_list_products', blank=True)

    def __str__(self):
        return self.user.username
