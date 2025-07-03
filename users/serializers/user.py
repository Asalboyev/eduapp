from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from rest_framework.serializers import ModelSerializer, Serializer
from rest_framework.fields import EmailField, IntegerField, CharField

from users.models import User


class RegisterModelSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        username = email.split('@')[0]

        user = User(
            email=email,
            username=username,
        )
        user.set_password(password)
        user.save()
        return user


class RegisterCheckSerializer(Serializer):
    code = IntegerField(required=True)

    def validate(self, data):
        email = self.context["request"].user.email
        verify_code = cache.get(email)
        
        if not verify_code:
            raise ValidationError({"code": "Tasdiqlash kodi eskirgan yoki noto‘g‘ri!"})
        
        if str(data["code"]) != str(verify_code):
            raise ValidationError({"code": "Noto‘g‘ri kod!"})
        
        return data
    

class ResendCodeSerializer(Serializer):
    email = EmailField()
