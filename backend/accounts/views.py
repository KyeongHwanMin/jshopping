from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from .serializers import SignupSerializer


class SignupView(CreateAPIView):
    model = get_user_model() # 유저 모델이 바뀔 수 있기 때문에 선호
    serializer_class = SignupSerializer
    permission_classes = [
        AllowAny,
    ]

