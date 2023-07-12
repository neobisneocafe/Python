from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework import routers
from .views import RegisterView, LoginView, ProfileViewSet, UsersViewSet, VerificationView

users_router = routers.SimpleRouter()
users_router.register(r'users_profile', ProfileViewSet, basename='users_profile')
users_router.register(r'users_list', UsersViewSet, basename='users_list')


urlpatterns = [

    path("", include(users_router.urls)),
    path("register/", RegisterView.as_view()),
    path("send_code/", VerificationView.as_view()),
    path("login/", LoginView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("obtain/", TokenObtainPairView.as_view()),
]
