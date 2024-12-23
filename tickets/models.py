from django.db import models
from django.conf import settings
# Create your models here.

class ScannedReceipt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255, blank=True)
    date = models.DateField(null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Asegúrate de que permite nulos
    image = models.ImageField(upload_to='scanned_receipts/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Receipt from {self.store_name or 'Unknown'} on {self.date or 'Unknown'}"
