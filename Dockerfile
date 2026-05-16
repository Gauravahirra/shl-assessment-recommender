FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Run catalog scraper at startup if catalog.json doesn't exist
# Otherwise use static catalog from catalog_data.py
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
