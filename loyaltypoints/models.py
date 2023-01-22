from django.db import models
from checkout.models import Order
from django.contrib.auth.models import User


class LoyaltyPoints(models.Model):
    """
    A user profile model for maintaining default
    delivery information and order history
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    points = models.IntegerField(blank=False, null=False)

    @classmethod
    def create(cls, user, order, points):
        loyalty = cls(user=user, order=order, points=points)
        return loyalty

    def __str__(self):
        return f"{self.user.username} {self.order.order_number} {self.points}"
