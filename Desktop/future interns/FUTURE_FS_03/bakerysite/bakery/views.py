from django.shortcuts import render, redirect
from .models import Product, Testimonial, Order, Contact, CartItem, Category
from django.db.models import Q

def home(request):
    popular_products = Product.objects.filter(is_popular=True)[:6]
    reviews = Testimonial.objects.all()[:6]

    return render(request, "bakery/home.html", {
        "popular_products": popular_products,
        "reviews": reviews
    })


def menu(request):
    category_id = request.GET.get("category")
    query = request.GET.get("q")

    products = Product.objects.all()

    if category_id:
        products = products.filter(category_id=category_id)

    if query:
        products = products.filter(name__icontains=query)

    categories = Category.objects.all()

    return render(request, "bakery/menu.html", {
        "products": products,
        "categories": categories
    })


def order(request):
    if request.method == "POST":
        Order.objects.create(
            customer_name=request.POST['name'],
            phone=request.POST['phone'],
            product=request.POST['product'],
            message=request.POST.get('message', '')
        )
        return redirect('home')

    return render(request, 'bakery/order.html')


def contact(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            message=request.POST['message']
        )
        return redirect('home')

    return render(request, 'bakery/contact.html')


def add_to_cart(request, product_id):

    product = Product.objects.get(id=product_id)

    item, created = CartItem.objects.get_or_create(product=product)

    if not created:
        item.quantity += 1
        item.save()

    return redirect("cart")


def cart(request):

    items = CartItem.objects.all()

    total = sum(item.total_price() for item in items)

    return render(request, "bakery/cart.html", {
        "items": items,
        "total": total
    })


def remove_item(request, item_id):
    CartItem.objects.get(id=item_id).delete()
    return redirect("cart")