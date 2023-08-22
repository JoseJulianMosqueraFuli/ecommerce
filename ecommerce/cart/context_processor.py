from .cart import Cart


def cart_context_session(request):
    return {"cart": Cart(request)}
