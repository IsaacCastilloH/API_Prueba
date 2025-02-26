FROM python:latest

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean \

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]