from django.db import models

class Sale(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    barcode = models.CharField(max_length=255, name='barcode')
    price = models.IntegerField(name='price')
    quantity = models.IntegerField(name='quantity')
    time = models.DateTimeField(name='sale_time')

    class Meta:
        db_table = 'sale'

class Supply(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    barcode = models.CharField(max_length=255, name='barcode')
    price = models.IntegerField(name='price')
    quantity = models.IntegerField(name='quantity')
    time = models.DateTimeField(name='supply_time')

    class Meta:
        db_table = 'supply'