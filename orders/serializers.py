from .models import Order
from rest_framework import serializers


class OrderCreationSerializers(serializers.ModelSerializer):

    # customer = serializers.ForeignKey()
    size = serializers.CharField(max_length=30,)
    order_status = serializers.CharField(max_length=30, default='PENDING')
    quantity = serializers.IntegerField(default=1)

    class Meta:
        model = Order
        fields = ['id','size', 'order_status', 'quantity']


class OrderDetailSerializers(serializers.ModelSerializer):

    # customer = serializers.ForeignKey()
    size = serializers.CharField()
    order_status = serializers.CharField()
    quantity = serializers.IntegerField(default=1)

    updated_at = serializers.DateTimeField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['id','size', 'order_status',
                  'quantity', 'created_at', 'updated_at']


class OrderUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField()
    updated_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['order_status', 'updated_at']
