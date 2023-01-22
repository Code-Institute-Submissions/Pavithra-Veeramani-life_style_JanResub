from django.shortcuts import render
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Subscription
from .forms import SubscriptionForm


class SubscriptionView(View):
    """
    Handle GET and POST requests for subscription
    """

    def post(self, request):
        """
        This method is called when a POST request is made to the view
        via the subscription form
        """
        email = request.POST['email']
        print(('email', email))
        if email:
            if Subscription.objects.filter(email=email).exists():
                messages.error(
                    request,
                    f"{email} is already subscribed."
                )
            else:
                sub = Subscription.create(email)
                sub.save()
                messages.success(self.request, 'Subscription created successfully.')

            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
