from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Incluye las rutas de la app users
    path('api/transactions/', include('transactions.urls')),  # Incluye las rutas de la app transactions
    path('api/subscriptions/', include('subscriptions.urls')),  # Incluye las rutas de la app subscriptions
]
