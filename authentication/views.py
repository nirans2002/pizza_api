from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import User
from . import serializers

# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    def get(self, request):
        return Response(data = {'message': 'Hello, World!'},status=status.HTTP_200_OK)

class UserCreateView(generics.GenericAPIView):
    serializer_class = serializers.CustomUserCreationSerializer
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)