from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchesViewSet, IngredientsViewSet, ReadyProductsViewSet


router = DefaultRouter()
router.register(r'branches', BranchesViewSet, basename='branches')
router.register(r'ready_products', ReadyProductsViewSet, basename='ready_products')
router.register(r'ingredients', IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path("", include(router.urls)),
]
