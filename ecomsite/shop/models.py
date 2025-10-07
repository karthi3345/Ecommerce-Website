# models.py in your app (e.g. shop)

from django.db import models

class Products(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount_price = models.FloatField(null=True, blank=True)
    category = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=500, null=True, blank=True)  # Renamed to 'image'
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation

    def __str__(self):
        return self.title


class Orders(models.Model):
    product = models.ForeignKey('Products', on_delete=models.CASCADE, related_name='orders')  # FK relationship
    quantity = models.IntegerField()
    total_price = models.FloatField()
    created_at_order = models.DateTimeField(auto_now_add=True)  # Timestamp of order creation

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order #{self.id}"
