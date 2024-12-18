FROM python:3.10-slim
WORKDIR /ExpenseTracker
COPY requirements.txt /ExpenseTracker/
RUN pip install -r requirements.txt
COPY . /ExpenseTracker/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
