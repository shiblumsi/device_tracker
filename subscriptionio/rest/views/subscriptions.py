from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser
from subscriptionio.models import SubscriptionPlan
from subscriptionio.rest.serializers.subscription import SubscriptionPlanSerializer

class SubscriptionPlanListCreateAPIView(ListCreateAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUser]

class SubscriptionPlanRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubscriptionPlan.objects.all()
    serializer_class = SubscriptionPlanSerializer
    permission_classes = [IsAdminUser]