from rest_framework import serializers

from ..models import CommodityTransaction


class CommodityTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommodityTransaction
        fields = '__all__'
