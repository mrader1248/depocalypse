from django.contrib import admin
from ..models import CommodityTransaction


class CommodityTransactionAdmin(admin.ModelAdmin):
    list_display = [
        CommodityTransaction.id.field.name,
        CommodityTransaction.transaction_timestamp.field.name,
        CommodityTransaction.commodity.field.name,
        CommodityTransaction.amount.field.name,
        CommodityTransaction.best_before_date.field.name,
    ]


admin.site.register(CommodityTransaction, CommodityTransactionAdmin)
