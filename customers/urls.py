from django.urls import path

from customers.views import BasketView, ContactView, OrderView

app_name = 'customers'
urlpatterns = [
    path('contact', ContactView.as_view(), name='user-contact'),
    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),
]
