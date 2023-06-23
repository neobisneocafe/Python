from django.urls import include, path
from rest_framework import routers
from .views import OrderViewSet, MenuItemViewSet, UserProfileViewSet, NotificationViewSet, WorkScheduleViewSet

router = routers.SimpleRouter()
router.register(r'orders', OrderViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'work-schedule', WorkScheduleViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
