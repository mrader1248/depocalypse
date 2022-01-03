from collections import defaultdict
from itertools import accumulate

from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Commodity, CommodityTransaction


@api_view(['GET'])
def calorific_value_over_time(request):

    kcal_by_commodity_id = {
        commodity.id: commodity.calorific_value_in_kcal 
        for commodity in Commodity.objects.all()
    }

    kcal_change_by_date = defaultdict(lambda: 0)
    kcal_remaining_by_commodity_id_and_best_before_date = defaultdict(lambda: 0)

    for commodity_transaction in CommodityTransaction.objects.all():
        kcal = commodity_transaction.amount * kcal_by_commodity_id[commodity_transaction.commodity_id]
        kcal_change_by_date[commodity_transaction.transaction_timestamp.date()] += kcal
        kcal_remaining_by_commodity_id_and_best_before_date[
            commodity_transaction.commodity_id, 
            commodity_transaction.best_before_date
        ] += kcal
    
    for (commodity_id, best_before_date), kcal in kcal_remaining_by_commodity_id_and_best_before_date.items():
        kcal_change_by_date[best_before_date] -= kcal
    
    dates = sorted(kcal_change_by_date)
    total_kcal_values = accumulate(kcal_change_by_date[date] for date in dates)
    return Response([
        {date.isoformat(): kcal}
        for date, kcal in zip(dates, total_kcal_values)
    ])
