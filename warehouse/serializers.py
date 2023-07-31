from .models import Ingredients, ReadyProducts, Branches
from rest_framework import serializers


class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'


class ReadyProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReadyProducts
        fields = '__all__'


class IngredientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients
        fields = '__all__'
