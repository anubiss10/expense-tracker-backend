from rest_framework.viewsets import ModelViewSet
from .models import Subscription
from .serializers import SubscriptionSerializer
from rest_framework.permissions import IsAuthenticated

class SubscriptionViewSet(ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
