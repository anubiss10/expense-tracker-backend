from django.db import models
from django.conf import settings

class Subscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    recurring = models.BooleanField(default=True)
    interval = models.CharField(max_length=20, choices=[('daily', 'Daily'), ('monthly', 'Monthly'), ('yearly', 'Yearly')])

    class Meta:
        unique_together = ('user', 'name')
        
    def __str__(self):
        return f"{self.name} - {self.amount}"
