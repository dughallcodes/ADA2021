from django.shortcuts import render
from rest_framework import viewsets
from .models import User, Courier
from .serializers import UserSerializer, CourierSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.exceptions import ObjectDoesNotExist
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated

from users import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["uuid"] = user.id
        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class CourierViewSet(viewsets.ModelViewSet):
    queryset = Courier.objects.all()
    serializer_class = CourierSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LoginUserViewSet(viewsets.ViewSet):
    def create(self, request):
        req_data = request.data
        if "username" in req_data and "password" in req_data:
            username = req_data["username"]
            password = req_data["password"]
            try:
                new_user = (
                    User.objects.filter(username=username)
                    .filter(password=password)
                    .get()
                )
            except ObjectDoesNotExist:
                return Response(status=404, data={"error": "User not found"})

            refresh = RefreshToken.for_user(new_user)
            return Response(
                status=200,
                data={
                    "token": str(refresh.access_token),
                    "username": username,
                },
            )

        else:
            return Response(
                status=400,
                data={
                    "error": "Invalid request format, expected format is {'username':'username_value','password':'password_value'}"
                },
            )


class LoginCourierViewSet(viewsets.ViewSet):
    def create(self, request):
        req_data = request.data
        if "username" in req_data and "password" in req_data:
            username = req_data["username"]
            password = req_data["password"]
            try:
                new_user = (
                    Courier.objects.filter(username=username)
                    .filter(password=password)
                    .get()
                )
            except ObjectDoesNotExist:
                return Response(status=404, data={"error": "User not found"})
            refresh = RefreshToken.for_user(new_user)
            return Response(
                status=200,
                data={
                    "token": str(refresh.access_token),
                    "username": username,
                },
            )
        else:
            return Response(status=400, data={"error": "Invalid request format"})
