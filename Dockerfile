FROM python:3.11

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask_cors

COPY src/ .
COPY config.json .


EXPOSE 5000

CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]