from .models import Order
from rest_framework import serializers


class OrderCreationSerializers(serializers.ModelSerializer):

    # customer = serializers.ForeignKey()
    size= serializers.CharField(max_length=30,)
    order_status= serializers.CharField(max_length=30,default='PENDING')
    quantity= serializers.IntegerField(default=1)

    class Meta:
        model = Order
        fields = ('size', 'order_status', 'quantity')
