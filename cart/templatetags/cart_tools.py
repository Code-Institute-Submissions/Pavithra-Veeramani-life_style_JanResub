from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_suibtotal(price, quantity):
    return price * quantity