from ..models.commodity import Commodity


def create_commodity_with_transactions(name, calorific_value_in_kcal, transactions):
    commodity = Commodity.objects.create(
        name=name,
        calorific_value_in_kcal=calorific_value_in_kcal
    )

    for transaction_timestamp, amount, best_before_date in transactions:
        commodity.commoditytransaction_set.create(
            transaction_timestamp=transaction_timestamp,
            amount=amount,
            best_before_date=best_before_date
        )

    return commodity
