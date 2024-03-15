from django.urls import path
from deviceio.rest.views import checkout

app_name = 'checkout'

urlpatterns = [
    path('checkout/create', checkout.CheckoutCreateView.as_view(),name='checkout-create'),
    path('checkout/list', checkout.CheckoutListView.as_view(),name='checkout-list'),
    path('checkout/detail/<uuid:uuid>', checkout.CheckoutRetrieveUpdateDestroyView.as_view(),name='checkout.detail.update.destroy'),
]
