from django.contrib import admin
from .models import Date, Trade

# unnecessary but good for learning, will eventually delete...


class TradeAdmin(admin.ModelAdmin):
    list_display = (
        'symbol',
        'open_close',
        'side',
        'type',
        'quantity',
        'share_price',
        'cost_basis',
        'pnl'
    )
    exclude = ('date_created', )


# Register your models here.
admin.site.register(Date)
admin.site.register(Trade, TradeAdmin)
