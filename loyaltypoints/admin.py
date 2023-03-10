from django.contrib import admin

from .models import LoyaltyPoints


class LoyaltyPointsAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'order',
        'points',
        'redeemed_flag'
    )


admin.site.register(LoyaltyPoints, LoyaltyPointsAdmin)
