from django.db import models

# Create your models here.
# By inheriting from the Models class, we don't have to write a bunch of
# code for storing data in a database


class DateTradePlace(models.Model):
    date_placed = models.DateField(max_length=255)


class Trade(models.Model):
    open_close = models.CharField(max_length=255)
    side = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    share_price = models.FloatField()
    cost_basis = models.FloatField()
    pnl = models.FloatField()
    date_placed = models.ForeignKey(DateTradePlace, on_delete=models.CASCADE)
