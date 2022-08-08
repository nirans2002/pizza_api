from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import CustomUser
from . import serializers
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
class HelloAuthView(generics.GenericAPIView):
    @swagger_auto_schema(operation_summary='Create a new user')

    def get(self, request):
        return Response(data = {'message': 'Hello, World!'},status=status.HTTP_200_OK)

class UserCreateView(generics.GenericAPIView):
    
    serializer_class = serializers.CustomUserCreationSerializer
    @swagger_auto_schema(operation_summary='Create a new user',)
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)


        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
