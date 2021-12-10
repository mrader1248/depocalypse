from django.urls import path

from .views import CommodityTransactionViewSet, CommodityViewSet, inventory

urlpatterns = [
    path('commodity/', CommodityViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('commodity/<int:pk>/', CommodityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('commodity-transaction/', CommodityTransactionViewSet.as_view({'post': 'create'})),
    path('inventory/', inventory),
]
