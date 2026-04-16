FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080 8000

CMD sh -c "python -m uvicorn api.main:app --app-dir code/backend --host 0.0.0.0 --port 8000 & python -m http.server 8080 --directory code/frontend"
