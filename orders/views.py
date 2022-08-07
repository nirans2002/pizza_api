from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response

from orders.serializers import OrderCreationSerializers
from .models import Order
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class HelloOrderView(generics.GenericAPIView):
    def get(self, request):
        return Response(data={'message': 'Hello, order!'}, status=status.HTTP_200_OK)


class OrderCreationView(generics.GenericAPIView):

    serializer_class = OrderCreationSerializers
    queryset = Order.objects.all()

    permission_classes=[
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
            serializer.save(customer= user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderDetailView(generics.GenericAPIView):

    def get(self, request, order_id):
        pass

    def post(self, request, order_id):
        pass

    def delete(self, request, order_id):
        pass
