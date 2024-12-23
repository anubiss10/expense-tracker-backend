from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from ExpenseTracker import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Incluye las rutas de la app users
    path('api/transactions/', include('transactions.urls')),  # Incluye las rutas de la app transactions
    path('api/subscriptions/', include('subscriptions.urls')),  # Incluye las rutas de la app subscriptions
    path('api/tickets/', include('tickets.urls')), #Incliye las rutas del scaneo de tickets

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
