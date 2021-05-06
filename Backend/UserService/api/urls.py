"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import routers
from django.urls import path
from users import views
from django.urls.conf import include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router_register = routers.DefaultRouter()
router_login = routers.DefaultRouter()
router_get_address = routers.DefaultRouter()
router_register.register(r"user", views.UserViewSet, basename="Register User")
router_register.register(r"courier", views.CourierViewSet, basename="Register Courier")
router_login.register(r"user", views.LoginUserViewSet, basename="Login User")
router_login.register(r"courier", views.LoginCourierViewSet, basename="Login User")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", include(router_register.urls)),
    path("login/", include(router_login.urls)),
]
