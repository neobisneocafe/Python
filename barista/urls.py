from django.urls import include, path
from rest_framework import routers
from .views import OrderViewSet, MenuViewSet, UserProfileViewSet

router = routers.DefaultRouter()
router.register(r'orders', OrderViewSet)
router.register(r'menu', MenuViewSet)
router.register(r'user-profile', UserProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
