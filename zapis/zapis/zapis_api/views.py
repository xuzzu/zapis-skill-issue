from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SaleSerializer, SupplySerializer
from .models import Sale
from .models import Supply

from django.http import JsonResponse

### FOR SALES ###

class SaleView(APIView):
    def get(self, request, id=None):
        # If we pass Id in the URL, we get the sale with that Id
        if id:
            sale = Sale.objects.get(id=id)
            serializer = SaleSerializer(sale)
            return Response(serializer.data)

        # If we don't pass Id in the URL, we get all the sales with optional filtering
        barcode = request.GET.get('barcode')
        from_time = request.GET.get('fromTime')
        to_time = request.GET.get('toTime')

        sales = Sale.objects.all()

        if barcode:
            sale = sales.filter(barcode=barcode)
        if from_time:
            sale = sales.filter(sale_time__gte=from_time)
        if to_time:
            sale = sales.filter(sale_time__lte=to_time)

        serializer = SaleSerializer(sales, many=True)
        return Response(serializer.data)

class CreateSaleView(APIView):
    def post(self, request):
        serializer = SaleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateSaleView(APIView):
    def put(self, request, id):
        try:
            sale = Sale.objects.get(id=id)
        except Sale.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SaleSerializer(sale, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteSaleView(APIView):
    def delete(self, request, id):
        try:
            sale = Sale.objects.get(id=id)
        except Sale.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        sale.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

### FOR SUPPLY ###

class SupplyView(APIView):
    def get(self, request, id=None):
        # If we pass Id in the URL, we get the sale with that Id
        if id:
            supply = Supply.objects.get(id=id)
            serializer = SupplySerializer(supply)
            return Response(serializer.data)

        barcode = request.GET.get('barcode')
        from_time = request.GET.get('fromTime')
        to_time = request.GET.get('toTime')

        supply = Supply.objects.all()

        if barcode:
            supply = supply.filter(barcode=barcode)

        if from_time:
            supply = supply.filter(sale_time__gte=from_time)

        if to_time:
            supply = supply.filter(sale_time__lte=to_time)

        serializer = SupplySerializer(supply, many=True)
        return Response(serializer.data)

class CreateSupplyView(APIView):
    def post(self, request):
        serializer = SupplySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateSupplyView(APIView):
    def put(self, request, id):
        try:
            supply = Supply.objects.get(id=id)
        except Supply.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = SupplySerializer(supply, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteSupplyView(APIView):
    def delete(self, request, id):
        try:
            supply = Supply.objects.get(id=id)
        except Supply.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        supply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)