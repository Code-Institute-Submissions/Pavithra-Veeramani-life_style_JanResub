from django.shortcuts import render
from products.models import Brand


def all_brands(request):

    """ A view to show all brands, including sorting and search queries """

    brands = Brand.objects.all()
            
    context = {
        'brands': brands
    }

    return render(request, 'brands/brands.html', context)
