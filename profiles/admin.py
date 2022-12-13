from django.contrib import admin
from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_wish_list'
    )

    def get_wish_list(self, obj):
        return [p.id for p in obj.wish_list.all()]
    ordering = ('id',)
    

admin.site.register(UserProfile, UserProfileAdmin)