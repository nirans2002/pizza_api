from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from orders.serializers import OrderCreationSerializers, OrderDetailSerializers, OrderUpdateSerializer
from .models import Order
from rest_framework.permissions import IsAuthenticated
# Create your views here.

User = get_user_model()
class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Hello, order!'}, status=status.HTTP_200_OK)


class OrderCreationView(generics.GenericAPIView):

    serializer_class = OrderCreationSerializers
    queryset = Order.objects.all()

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):
        orders = Order.objects.all()

        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)

        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):
    permission_classes = [
        IsAuthenticated
    ]
    serializer_class = OrderDetailSerializers

    def get(self, request, order_id):
        order = get_object_or_404(Order, pk=order_id)
        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)

        serializer = self.serializer_class(data=data,instance=order)
        user = request.user

        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, order_id):
        data = request.data
        order = get_object_or_404(Order, pk=order_id)
        order.delete()

        return Response(data={'message': 'Order deleted'}, status=status.HTTP_204_NO_CONTENT)

class UpdateOrderStatus(generics.GenericAPIView):
    permission_classes = [
        IsAuthenticated
    ]

    serializer_class = OrderUpdateSerializer
    def put(self, request,order_id):
        order = get_object_or_404(Order, pk=order_id)
        data = request.data
        user = request.user

        serializer = self.serializer_class(instance=order, data=data)
        if serializer.is_valid():
            serializer.save(customer=user)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class UserOrdersView(generics.GenericAPIView):
    # permission_classes = [
    #     IsAuthenticated
    # ]

    serializer_class = OrderDetailSerializers

    def get(self, request,user_id):
        user = User.objects.get(pk=user_id)
        orders = Order.objects.all().filter(customer=user)
        serializer = self.serializer_class(instance=orders, many=True)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
    
class UserOrderDetail(generics.GenericAPIView):
    # permission_classes = [
    #     IsAuthenticated
    # ]

    serializer_class = OrderDetailSerializers

    def get(self, request
    ,user_id,order_id):
        user = User.objects.get(pk=user_id)
        order = Order.objects.all().filter(customer=user).get(pk=order_id)
        
        serializer = self.serializer_class(instance=order)

        return Response(data=serializer.data, status=status.HTTP_200_OK)