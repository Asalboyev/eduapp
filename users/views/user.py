from random import randint
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from django.http import JsonResponse
from drf_spectacular.utils import extend_schema
from rest_framework.generics import CreateAPIView, GenericAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND
from rest_framework.views import APIView

from users.models import User
from users.serializers import RegisterModelSerializer
from users.serializers.user import RegisterCheckSerializer

from users.tasks import send_email


@extend_schema(tags=['auth'], request=RegisterModelSerializer)
class RegisterAPIView(CreateAPIView):
    serializer_class = RegisterModelSerializer

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        user = User.objects.filter(email=email).first()

        if user and user.is_active:
            return JsonResponse({"message": "Email oldin ro'yxatdan o'tgan!"}, status=HTTP_400_BAD_REQUEST)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if not user:
                user = serializer.save()

            random_code = randint(10000, 99999)
            send_email.delay(email, random_code)
            cache.set(email, str(random_code), timeout=300)

            refresh = RefreshToken.for_user(user)
            return Response({
                "message": f"{email} manziliga tasdiqlash kodi jo'natildi!",
                "access": str(refresh.access_token),
                "refresh": str(refresh)
            }, status=HTTP_200_OK)

        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)


@extend_schema(tags=['auth'], request=RegisterCheckSerializer)
class RegisterCheckAPIView(GenericAPIView):
    serializer_class = RegisterCheckSerializer
    permission_classes = [IsAuthenticated]


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            email = request.user.email
            updated = User.objects.filter(email=email).update(is_verify=True)
            if updated:
                cache.delete(email)
                return JsonResponse(
                    {"message": "Ro‘yxatdan o‘tish muvaffaqiyatli!"},
                    status=HTTP_200_OK
                )
            return JsonResponse(
                {"error": "Foydalanuvchi topilmadi"},
                status=HTTP_404_NOT_FOUND
            )
        return JsonResponse(serializer.errors, status=HTTP_400_BAD_REQUEST)
