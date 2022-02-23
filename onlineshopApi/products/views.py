from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Product
from order.models import Order, OrderItem
from django.views.generic import ListView, DetailView


class HomeView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'items'




class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'


def add_to_cart(request, slug):
    item = get_object_or_404(Product, slug=slug)
    orderitem = OrderItem.objects.create(order=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.products.filter(item_slug=item.slug).exists():
            orderitem.quantity += 1
            orderitem.save()
    else:
        order = Order.objects.create(user=request.user)
        order.items.add(orderitem)


def checkout(request):
    context = {
        'orders': Order.objects.all(),
    }
    return render(request, 'checkout-page.html', context=context)


from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)
    return render(request,
                  'product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    return render(request,
                  'shop/product/detail.html',
                  {'product': product})


# def checkoutView(request):
#     context = {
#
#     }
#     return render(request, 'checkout.html', context=context)
class CheckoutView(CreateView):
    model = Order
    template_name = 'products/checkout-page.html'
