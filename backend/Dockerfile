FROM python:3.9-slim

# Создает директорию /app внутри контейнера и делает её рабочей
WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    # Компилятор C (нужен для сборки некоторых Python-пакетов)
    gcc \
    # Заголовочные файлы Python
    python3-dev \
    # Удаляет кеш пакетов
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
# Копирует файл requirements.txt из локальной папки в /app внутри контейнера.
COPY requirements.txt .
# Отключаем кеш (--no-cache-dir), для уменьшения размера образа.
RUN pip install --no-cache-dir -r requirements.txt

# Копирование кода, модели и токенизатора
COPY *.py ./
COPY production_model/ ./production_model/

# Запуск приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]