from .cart import Cart

from datetime import datetime

def cart_context(request):
    return {'cart' :Cart(request)}



def time(request):
    return {'time':datetime.now()}