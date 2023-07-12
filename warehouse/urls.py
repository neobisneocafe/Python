from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BranchesViewSet, WareHouseViewSet, CategoryViewSet


router = DefaultRouter()
router.register(r'branches', BranchesViewSet, basename='branches')
router.register(r'warehouse', WareHouseViewSet, basename='warehouse')
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = [
    path("", include(router.urls)),
]