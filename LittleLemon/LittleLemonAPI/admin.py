from django.contrib import admin
from .models import MenuItem, OrderItem, Order, Category, Cart

admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(MenuItem)
admin.site.register(OrderItem)
admin.site.register(Order)
