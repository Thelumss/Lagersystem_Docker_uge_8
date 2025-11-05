FROM python:3.11

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask_cors

COPY . .
COPY ../config.json ./config.json


EXPOSE 5000

CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]