from django.urls import path

from .views import CommodityTransactionViewSet, CommodityViewSet, calorific_value_outlook, inventory

urlpatterns = [
    path('calorific-value-outlook/', calorific_value_outlook),
    path('commodity/', CommodityViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('commodity/<int:pk>/', CommodityViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    path('commodity-transaction/', CommodityTransactionViewSet.as_view({'post': 'create'})),
    path('inventory/', inventory),
]
