from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category, Brand
from wishlist.models import WishList
from .forms import ProductForm
from reviews.forms import ReviewForm
from reviews.models import Review


def all_products(request):

    """
    A view to show all products, including sorting and search queries
    Also filters products based on category, brand, wishlist
    """

    products = Product.objects.all()
    query = None
    categories = None
    brands = None
    sort = None
    order = None
    wishlist_products = None

    if not request.user.is_anonymous:
        try:
            wishlist = WishList.objects.get(user=request.user)
            wishlist_products = [p.id for p in wishlist.products.all()]
        except WishList.DoesNotExist:
            wishlist_products = []
    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'order' in request.GET:
                order = request.GET['order']
                if order == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)
        if 'brand' in request.GET:
            brands = request.GET['brand'].split(',')
            products = products.filter(brand__name__in=brands)
            brands = Brand.objects.filter(name__in=brands)
        if 'wishlist' in request.GET and wishlist_products is not None:
            products = products.filter(pk__in=wishlist_products)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)
    current_sorting = f'{sort}_{order}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'wishlist': wishlist_products
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):

    """ A view to show individual product details"""

    product = get_object_or_404(Product, pk=product_id)
    # reviews = post.comments.filter(approved=True).order_by("-created_on")
    reviews = Review.objects.filter(product=product)
    current_user_review_flag = False
    for review in reviews:
        if review.created_by == request.user:
            current_user_review_flag = True

    product_in_wishlist = False

    if not request.user.is_anonymous:
        try:
            wishlist = WishList.objects.get(user=request.user)
            wishlist_products = [p.id for p in wishlist.products.all()]
            for wl_prod in wishlist_products:
                if wl_prod == product_id:
                    product_in_wishlist = True
        except WishList.DoesNotExist:
            product_in_wishlist = False

    context = {
        'product': product,
        'reviews': reviews,
        'current_user_review_flag': current_user_review_flag,
        'product_in_wishlist': product_in_wishlist,
        'review_form': ReviewForm()
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """Add aproduct to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.')
    else:
        form = ProductForm()
    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
