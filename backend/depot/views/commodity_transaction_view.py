from rest_framework import viewsets

from ..models import CommodityTransaction
from ..serializers import CommodityTransactionSerializer


class CommodityTransactionViewSet(viewsets.ModelViewSet):
    queryset = CommodityTransaction.objects.all()
    serializer_class = CommodityTransactionSerializer
