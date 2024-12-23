from django.db import models
from django.conf import settings
from django.utils.timezone import now
from datetime import timedelta

FREQUENCY_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('yearly', 'Yearly'),
]

class Subscription(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='subscriptions'
    )
    name = models.CharField(max_length=255)
    cost = models.FloatField()
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES,null=True, blank=True)
    start_date = models.DateField(default=now)
    next_renewal_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Calcular la próxima fecha de renovación según la frecuencia
        if not self.next_renewal_date:
            self.next_renewal_date = self.calculate_next_renewal_date()
        super().save(*args, **kwargs)

    def calculate_next_renewal_date(self):
        if self.frequency == 'daily':
            return self.start_date + timedelta(days=1)
        elif self.frequency == 'weekly':
            return self.start_date + timedelta(weeks=1)
        elif self.frequency == 'monthly':
            return self.start_date + timedelta(days=30)
        elif self.frequency == 'yearly':
            return self.start_date + timedelta(days=365)
        return self.start_date

    def __str__(self):
        return f"{self.name} - {self.cost} ({self.frequency})"
