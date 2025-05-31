FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Сначала устанавливаем numpy 1.x
RUN pip install numpy==1.24.4

# Затем ключевые зависимости
RUN pip install \
    torch==2.0.1 \
    transformers==4.30.2 \
    safetensors==0.3.1 \
    nltk==3.8.1 \
    pymorphy3==1.1.0

# Остальные зависимости
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY *.py ./
COPY production_model/ ./production_model/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]