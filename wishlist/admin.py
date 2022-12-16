from django.contrib import admin

from .models import WishList


class WishListAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_products'
    )

    def get_products(self, obj):
        return [p.id for p in obj.products.all()]
    ordering = ('id',)


admin.site.register(WishList, WishListAdmin)
