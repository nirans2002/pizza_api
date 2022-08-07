from django.contrib import admin
from .models import Order
# Register your models here.


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'size', 'order_status', 'quantity', 'created_at', 'updated_at')

    list_filter = ('order_status', 'size','customer')