from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuCategoryViewSet,MenuItemViewSet,ProductViewSet


router = DefaultRouter()
router.register(r'menu-categories',MenuCategoryViewSet, basename='menu-category')
router.register(r'products',ProductViewSet, basename='product')
router.register(r'menu-items',MenuItemViewSet, basename='menuitem')


urlpatterns = [
    path("", include(router.urls)),
]