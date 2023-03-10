from django.shortcuts import redirect
from products.models import Product
from wishlist.models import WishList
from django.contrib import messages


def add_product_to_user_wish_list(request, id):
    wishlist = WishList.objects.filter(user=request.user).first()
    product = Product.objects.get(pk=id)
    if wishlist is None:
        wishlist_save = WishList(user=request.user)
        wishlist_save.save()
        wishlist_save.products.set([product])
    else:
        wishlist.products.add(product)
    messages.success(request, 'Product added to Wishlist.')
    return redirect(request.META.get('HTTP_REFERER'))


def delete_product_from_user_wish_list(request, id):
    wishlist = WishList.objects.filter(user=request.user).first()
    product = Product.objects.get(pk=id)
    wishlist.products.remove(product)
    messages.success(request, 'Product deleted from Wishlist.')
    return redirect(request.META.get('HTTP_REFERER'))
