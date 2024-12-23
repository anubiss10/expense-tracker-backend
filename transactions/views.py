from django.db.models import Sum,Q
from django.db.models.functions import TruncMonth
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models
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

    @action(detail=False, methods=['get'])
    def monthly_summary(self, request):
        # Agrupar por mes y sumar ingresos y gastos
        data = (
            Transaction.objects.filter(user=request.user)
            .annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(
                total_income=Sum('amount', filter=Q(transaction_type='income')),
                total_expense=Sum('amount', filter=Q(transaction_type='expense'))
            )
            .order_by('month')
        )
        return Response(data)
