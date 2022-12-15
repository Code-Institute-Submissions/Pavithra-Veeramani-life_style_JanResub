from django.urls import path, include
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('add/<int:id>', views.add_product_to_user_wish_list, name='add_product_to_user_wish_list'),
    path('remove/<int:id>',  views.delete_product_from_user_wish_list, name='delete_product_from_user_wish_list'),
]