from django.db import models
from django.utils import timezone
from . import Commodity


class CommodityTransaction(models.Model):
    transaction_timestamp = models.DateTimeField(default=timezone.now)
    commodity = models.ForeignKey(Commodity, on_delete=models.PROTECT)
    amount = models.IntegerField()
    best_before_date = models.DateField()

    def __str__(self):
        return (
            f'{self.amount:+d} "{self.commodity.name}" (#{self.commodity.id})'
            f', {self.transaction_timestamp}'
            f', best before {self.best_before_date}'
        )
