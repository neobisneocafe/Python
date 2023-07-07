from django.urls import path
from .views import BranchesListView,BranchesDetailView,WarehouseDetailView,WareHouseListView,CategoryListView\
    ,CategoryDetailView,WarehouseDeleteView


urlpatterns = [
    path('branches/', BranchesListView.as_view(), name='branches-list'),
    path('branches/<int:pk>/', BranchesDetailView.as_view(), name='branches-detail'),
    path('warehouse/', WareHouseListView.as_view(), name='warehouse-list'),
    path('warehouse/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse-detail'),
    path('warehouse/<int:pk>/delete/', WarehouseDeleteView.as_view(), name='warehouse-delete'),
    path('category/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]