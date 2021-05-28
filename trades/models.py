from django.db import models
from django.utils import timezone

# Create your models here.
# By inheriting from the Models class, we don't have to write a bunch of
# code for storing data in a database

# Model class gives us a bunch methods for creating, retrieving, UPDATING,
# entries from our database. (save method used for updating)


class Date(models.Model):
    date_placed = models.DateField(max_length=255)

    def __str__(self):
        return str(self.date_placed)


class Trade(models.Model):
    open_close = models.CharField(max_length=255)
    side = models.CharField(max_length=255)
    symbol = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    share_price = models.FloatField()
    cost_basis = models.FloatField()
    pnl = models.FloatField(blank=True, null=True)
    date_placed = models.ForeignKey(Date, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)


# import pymysql
# import os
# from alpaca import daily_closed_market, daily_closed_trailing_stops
# from dotenv import load_dotenv

# load_dotenv()
# DJANGO_ADMIN_SECRET_KEY = os.getenv('DJANGO_ADMIN_SECRET_KEY')

# connection = pymysql.connect(
#     host='127.0.0.1',
#     user='admin',
#     password=DJANGO_ADMIN_SECRET_KEY,
#     db='trades_trade'
# )

# cursor = connection.cursor()

# sql = "INSERT INTO 'trades_trade' ('open_close', 'side', 'symbol', 'type', 'quantity', 'share_price', 'cost_basis', 'pnl') VALUES (%s, %s, %s, %s, %s, %s)"

# cursor.execute(sql, ('OPEN', 'LONG', 'XYZ', 'MARKET',
#                12, 23.45, 280.12, '', '2021-05-27'))
# connection.commit()
