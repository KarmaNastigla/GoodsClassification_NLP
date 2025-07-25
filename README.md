# Классификация поисковых запросов для 21vek.by

Проект для автоматической категоризации поисковых запросов интернет-магазина 21vek.by с использованием BERT.

## 📌 О проекте

Система анализирует текстовые запросы пользователей и относит их к одной из товарных категорий. Это помогает:
- Улучшить поиск по сайту
- Оптимизировать навигацию
- Персонализировать рекомендации

## 📊 Данные
Обучающие данные содержат:
- 150K+ поисковых запросов
- 42 товарные категории
- Несбалансированное распределение классов

## 🧠 Модель классификации
Архитектура:
Fine-tuned BERT-base-multilingual (12 слоев, 110M параметров)

Метрики:
- Macro F1-score
- Accuracy

Особенности обработки текста:
- Лемматизация русских слов
- Удаление стоп-слов
- Очистка от специальных символов

## 🛠 Технологии

**Backend:**
- Python 3.9+
- PyTorch
- Transformers (BERT multilingual)
- Pymorphy3 (для лемматизации русского текста)
- FastAPI (REST API)

**Frontend:**
- Streamlit

**Инфраструктура:**
- Docker
- Git


## 🚀 Установка и запуск

### Требования
- Docker 20.10+
- Docker Compose 1.29+

### Быстрый запуск в Docker
```bash
git clone https://github.com/KarmaNastigla/GoodsClassification_NLP
cd GoodsClassification_NLP
docker-compose up --build
