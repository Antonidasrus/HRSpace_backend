FROM python:3.7-slim

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .

CMD ["gunicorn", "hrspace_backend.wsgi:application", "--bind", "0:8000" ]

# CMD ["python3", "manage.py", "runserver", "0:8000"] 