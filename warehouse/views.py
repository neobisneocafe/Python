from rest_framework import generics, status
from .models import Warehouse
from .serializers import WarehouseSerializer
from warehouse.models import Branches,Warehouse,Category
from warehouse.serializers import BranchesSerializer,WarehouseSerializer,CategorySerializer
from django.shortcuts import render, get_object_or_404
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


class BranchesListView(ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

class BranchesDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    lookup_field = 'pk'

class WareHouseListView(ListAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

class WarehouseDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer
    lookup_field = 'pk'

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class WarehouseDeleteView(generics.DestroyAPIView):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'pk'
