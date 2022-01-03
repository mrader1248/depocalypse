from django.db.models import Sum
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Commodity


@api_view(['GET'])
def inventory(request):
    commodities = (
        Commodity.objects
        .annotate(amount=Sum('commoditytransaction__amount'))
        .filter(amount__isnull=False, amount__gt=0)
    )
    response = [
        {
            'commodityId': commodity.id,
            'commodityName': commodity.name,
            'amount': commodity.amount,
            'totalCalorificValueInKcal': commodity.amount * commodity.calorific_value_in_kcal
        }
        for commodity in commodities
    ]
    return Response(response)
