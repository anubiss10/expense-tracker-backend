from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['post'])
    def renew_subscription(self, request):
        subscription_id = request.data.get('subscription_id')
        try:
            subscription = Subscription.objects.get(id=subscription_id, user=request.user)
            subscription.start_date = subscription.next_renewal_date
            subscription.next_renewal_date = subscription.calculate_next_renewal_date()
            subscription.save()
            return Response({"message": "Subscription renewed successfully!"})
        except Subscription.DoesNotExist:
            return Response({"error": "Subscription not found."}, status=404)