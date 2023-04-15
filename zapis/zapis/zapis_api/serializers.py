from rest_framework import serializers
from .models import Sale, Supply

### FOR SALES ###

class SaleSerializer(serializers.ModelSerializer):
    saleTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", source="sale_time")
    class Meta:
            model = Sale
            fields = ['id', 'barcode', 'price', 'quantity', 'saleTime']

### FOR SUPPLIES ###

class SupplySerializer(serializers.ModelSerializer):
    supplyTime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", source="supply_time")
    class Meta:
        model = Supply
        fields = ['id', 'barcode', 'quantity', 'price', 'supplyTime']