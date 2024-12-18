FROM python:3.10-slim

WORKDIR /ExpenseTracker

# Copiar dependencias y crear entorno
COPY requirements.txt /ExpenseTracker/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código del proyecto
COPY . /ExpenseTracker/

# Recolectar archivos estáticos para producción
RUN python manage.py collectstatic --noinput

# Ejecutar Gunicorn para servir el backend
CMD ["gunicorn", "ExpenseTracker.wsgi:application", "--bind", "0.0.0.0:8000"]
