from django.contrib import admin
from .models import Orders, Products

# Admin for Products
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'discount_price', 'category', 'image')
    list_filter = ('category',)
    search_fields = ('title', 'category')
    ordering = ('id',)

# Admin for Orders
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'quantity', 'total_price', 'status', 'created_at_order')
    list_filter = ('status', 'created_at_order')
    search_fields = ('product__title', 'status')
    ordering = ('created_at_order',)  # newest orders first

# Register models with admin
admin.site.register(Products, ProductsAdmin)
admin.site.register(Orders, OrdersAdmin)
