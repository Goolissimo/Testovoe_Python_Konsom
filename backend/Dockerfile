FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000

CMD uvicorn fastapi_app:app --host 0.0.0.0 --port 8000 --reload