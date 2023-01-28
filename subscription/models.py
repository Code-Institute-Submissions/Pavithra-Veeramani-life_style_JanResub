from django.db import models
from django.core.mail import send_mail
from django.conf import settings


class Subscription(models.Model):

    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    @classmethod
    def create(cls, email):
        subscription = cls(email=email)
        return subscription

    def __str__(self):
        return self.email


class Newsletter(models.Model):
    subject = models.CharField(max_length=150)
    contents = models.FileField(upload_to='uploaded_newsletters/')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject + " " + self.created_on.strftime("%B %d, %Y")

    def send(self, request):
        contents = self.contents.read().decode('utf-8')
        subscriptions = Subscription.objects.filter()
        subscriptions_emails = []
        for subscription in subscriptions:
            subscriptions_emails.append(subscription.email)
        print('subscriptions_emails', subscriptions_emails)
        send_mail(
            self.subject,
            contents,
            settings.EMAIL_HOST_USER,
            subscriptions_emails
        )
