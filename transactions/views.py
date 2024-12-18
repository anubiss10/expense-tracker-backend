from rest_framework.viewsets import ModelViewSet
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
