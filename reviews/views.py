from django.shortcuts import (
    render, redirect, reverse, get_object_or_404
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Review
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
        messages.success(request, 'Your product review has been submitted')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        messages.error(request, 'Failed to submit the review. \
            Please ensure the form is valid.')

    context = {
        'product': product,
        'form': form,
    }

    return render(request, template, context)