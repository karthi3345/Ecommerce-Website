from django.shortcuts import render
from .models import Products, Orders
from django.db.models import Sum
from django.utils import timezone
from datetime import timedelta

def dashboard(request):
    products_count = Products.objects.count()
    orders_count = Orders.objects.count()
    total_sales = Orders.objects.aggregate(Sum('total_price'))['total_price__sum'] or 0
    products = Products.objects.all()
    orders = Orders.objects.order_by('-created_at_order')[:10]
    notifications = Orders.objects.filter(status='Pending')[:5]
    notifications_count = notifications.count()

    # Sales data last 7 days
    labels = []
    sales_data = []
    for i in range(7, 0, -1):
        day = timezone.now().date() - timedelta(days=i)
        # Change 'created_at' to 'created_at_order'
        daily_sales = Orders.objects.filter(created_at_order__date=day).aggregate(Sum('total_price'))['total_price__sum'] or 0
        labels.append(day.strftime("%b %d"))
        sales_data.append(float(daily_sales))

    context = {
        'products_count': products_count,
        'orders_count': orders_count,
        'total_sales': total_sales,
        'products': products,
        'orders': orders,
        'notifications': notifications,
        'notifications_count': notifications_count,
        'labels': labels,
        'sales_data': sales_data
    }
    return render(request, 'shop/dashboard.html', context)

def product_list(request):
    products = Products.objects.all()
    return render(request, 'shop/product_list.html', {'products': products})
