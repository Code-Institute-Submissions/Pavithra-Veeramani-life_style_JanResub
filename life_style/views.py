from django.shortcuts import render, redirect, get_object_or_404
from profiles.models import UserProfile
from products.models import Product


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, "errors/404.html", status=404)


def add_product_to_user_wish_list(request, id):
    print('add wishlist')
    user = get_object_or_404(UserProfile, user=request.user)
    product = Product.objects.get(pk=id)
    wishlist = user.wish_list.add(product)
    return redirect('/products/')


def delete_product_from_user_wish_list(request, id):
    print('remove wishlist')
    user = get_object_or_404(UserProfile, user=request.user)
    product = Product.objects.get(pk=id)
    wishlist = user.wish_list.remove(product)
    return redirect('/products/')
