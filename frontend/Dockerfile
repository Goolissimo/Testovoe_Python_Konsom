FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r  requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "web_app.py"]
