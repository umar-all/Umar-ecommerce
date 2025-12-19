from django.shortcuts import render
from .models import Product

def home(request):
    if Product.objects.count() == 0:
        Product.objects.bulk_create([
            Product(
                name="Running Shoes",
                price=1999,
                description="Comfortable sports shoes",
                image="products/shoes.jpg"
            ),
            Product(
                name="Smart Watch",
                price=2999,
                description="Fitness tracking watch",
                image="products/watch.jpg"
            ),
            Product(
                name="Wireless Headphones",
                price=1499,
                description="Noise cancellation",
                image="products/headphones.jpg"
            ),
        ])

    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
