from django.db import models
from checkout.models import Order
from django.contrib.auth.models import User


class LoyaltyPoints(models.Model):
    """
    A model to represent a customer orders Loyalty points
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='loyaltypoints')
    points = models.IntegerField(blank=False, null=False)
    redeemed_flag = models.BooleanField(default=False)

    @classmethod
    def create(cls, user, order, points):
        loyalty = cls(user=user, order=order, points=points)
        return loyalty

    def __str__(self):
        return f"{self.user.username} {self.order.order_number} {self.points}"
