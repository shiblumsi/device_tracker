from django.urls import path
from subscriptionio.rest.views import purchase, subscriptions

urlpatterns = [
    path('subscription-plans/', subscriptions.SubscriptionPlanListCreateAPIView.as_view(), name='subscription-plan-list-create'),
    path('subscription-plans/<int:pk>/', subscriptions.SubscriptionPlanRetrieveUpdateDestroyAPIView.as_view(), name='subscription-plan-detail'),

    path('purchase/', purchase.PurchaseSubscriptionView.as_view(), name='purchase-subscription'),
]