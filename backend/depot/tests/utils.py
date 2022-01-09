import datetime
from ..models.commodity import Commodity


def create_commodity_with_transactions(
        name: str,
        calorific_value_in_kcal: int,
        transaction_data: list[tuple[datetime.datetime, int, datetime.date]]
) -> Commodity:
    """This function generates a `Commodity` object together with some
    associated `CommodityTransaction` objects.

    Args:
        name (str): The name of the `Commodity` object to be created.
        calorific_value_in_kcal (int): The calorific value of the
            `Commodity` object to be created.
        transaction_data: list[tuple[datetime.datetime, int, datetime.date]]:
            A list containing timestamps, amounts and best before dates of the
            transactions to be created.

    Returns:
        Commodity: The newly created `Commodity` object.
    """

    commodity = Commodity.objects.create(
        name=name,
        calorific_value_in_kcal=calorific_value_in_kcal
    )

    for timestamp, amount, best_before_date in transaction_data:
        commodity.commoditytransaction_set.create(
            transaction_timestamp=timestamp,
            amount=amount,
            best_before_date=best_before_date
        )

    return commodity
