from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'created_on'
    )


admin.site.register(Subscription, SubscriptionAdmin)
