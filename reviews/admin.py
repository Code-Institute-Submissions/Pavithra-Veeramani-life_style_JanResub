from django.contrib import admin

from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'created_by',
        'product',
        'content'
    )
admin.site.register(Review, ReviewAdmin)