from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Commodity


@api_view(['GET'])
def storage_list(request):
    commodities = Commodity.objects.prefetch_related('commoditytransaction_set').all()
    amount_per_commodity = {
        commodity.id: commodity.commoditytransaction_set.aggregate(Sum('amount'))['amount__sum'] or 0
        for commodity in commodities
    }
    response = [
        {
            'commodityName': commodity.name,
            'amount': amount_per_commodity[commodity.id],
            'totalCalorificValueInKcal': amount_per_commodity[commodity.id] * commodity.calorific_value_in_kcal
        }
        for commodity in commodities
    ]
    return Response(response)
