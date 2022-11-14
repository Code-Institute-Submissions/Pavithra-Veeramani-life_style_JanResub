from django.shortcuts import render

# Create your views here.


def view_cart(request):
    """ A view that renders the bag contents page """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified product to the shopping cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.GET('redirect_url')
    bag = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['bag'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)

