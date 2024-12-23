from django.urls import path
from .views import OCRView

urlpatterns = [
    path('scan/', OCRView.as_view(), name='scan-ticket'),
]
