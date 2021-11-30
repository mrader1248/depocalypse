from django.contrib import admin
from ..models import Commodity


class CommodityAdmin(admin.ModelAdmin):
    list_display = [
        Commodity.id.field.name,
        Commodity.name.field.name,
        Commodity.calorific_value_in_kcal.field.name
    ]


admin.site.register(Commodity, CommodityAdmin)
