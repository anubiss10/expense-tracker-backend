FROM python:3.10-slim

WORKDIR /ExpenseTracker

COPY requirements.txt /ExpenseTracker/
RUN pip install -r requirements.txt

COPY . /ExpenseTracker/

CMD ["gunicorn", "ExpenseTracker.wsgi:application", "--bind", "0.0.0.0:8000"]
