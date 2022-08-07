from .models import CustomUser
from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers


class CustomUserCreationSerializer(serializers.ModelSerializer):
    username =serializers.CharField(max_length=50)
    email =serializers.EmailField(max_length=255 )
    phone_no = PhoneNumberField(allow_blank=True,allow_null=False)
    password = serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username','email','phone_no','password')


    def validate(self,attrs):
        username_exists = CustomUser.objects.filter(username=attrs['username']).exists()
       

        if username_exists:
            raise serializers.ValidationError('username already exists')
        
        email_exists = CustomUser.objects.filter(email=attrs['email']).exists()
       

        if email_exists:
            raise serializers.ValidationError('email already exists')

        phone_no_exists = CustomUser.objects.filter(phone_no=attrs['phone_no']).exists()
       

        if phone_no_exists:
            raise serializers.ValidationError('phone number already exists')


        return super().validate(attrs)