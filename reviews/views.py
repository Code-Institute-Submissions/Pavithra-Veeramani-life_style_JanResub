from django.shortcuts import (
    redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from products.models import Product
from .forms import ReviewForm


@login_required
def create_review(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    form = ReviewForm(request.POST, request.FILES)
    if form.is_valid():
        form.instance.created_by = request.user
        form.instance.product = product
        form.save()
        messages.success(request, 'Review submitted successfully.')
    else:
        messages.error(request, 'Review submission failed.')

    return redirect(reverse('product_detail', args=[product.id]))
