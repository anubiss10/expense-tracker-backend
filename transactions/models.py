from django.core.exceptions import ValidationError
from django.db import models
from django.conf import settings

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    date = models.DateField()
    category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount}"

    def clean(self):
        if self.amount <= 0:
            raise ValidationError("El monto debe ser mayor que cero.")