from django.db import models
from django.contrib import admin

class GSTBill(models.Model):
    bill_id = models.IntegerField(primary_key=True)
    price = models.FloatField()
    gst = models.FloatField()
    gst_amount = models.FloatField()
    total_bill = models.FloatField()
    
class GSTBillAdmin(admin.ModelAdmin):
    list_display = ('bill_id', 'price', 'gst', 'gst_amount', 'total_bill')