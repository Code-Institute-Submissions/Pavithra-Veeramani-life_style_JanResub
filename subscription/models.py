from django.db import models


class Subscription(models.Model):

    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, email):
        subscription = cls(email=email)
        return subscription

    def __str__(self):
        return self.email
