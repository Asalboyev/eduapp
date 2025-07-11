from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from users.views.user import RegisterAPIView, RegisterCheckAPIView, ResendCodeAPIView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register', RegisterAPIView.as_view(), name='register'),
    path('register/check', RegisterCheckAPIView.as_view(), name='register_check'),
    path('resend-code/', ResendCodeAPIView.as_view(), name='resend-code'),


]