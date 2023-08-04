from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, WorkScheduleViewSet, BranchesViewSet

router = DefaultRouter()
router.register(r'branches', BranchesViewSet, basename='branch')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'work-shedules', WorkScheduleViewSet, basename='workshedule')

urlpatterns = [
    path("", include(router.urls)),
]