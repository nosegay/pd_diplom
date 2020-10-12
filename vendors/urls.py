from django.urls import path, include
from rest_framework import routers

from vendors.views import PartnerUpdate, CategoryView, ShopView, ProductInfoView, PartnerState, PartnerOrders

app_name = 'vendors'

router = routers.SimpleRouter()
router.register(r'products', ProductInfoView, basename='products')


urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),
    path('categories', CategoryView.as_view(), name='categories'),
    path('shops', ShopView.as_view(), name='shops'),
    path('', include(router.urls)),
]
