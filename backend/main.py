from fastapi import FastAPI
from pydantic import BaseModel
from model_utils import load_model, predict
import os

app = FastAPI(title="Text Classification API")

# Загрузка модели при старте
try:
    print("Loading model...")
    model, tokenizer, config = load_model()
    print("Model loaded successfully!")
except Exception as e:
    print(f"Failed to load model: {str(e)}")
    raise


class Query(BaseModel):
    text: str


class Prediction(BaseModel):
    category: str  # Теперь это будет текстовое название
    probability: float


@app.post("/predict", response_model=Prediction)
async def predict_text(query: Query):
    result = predict(query.text, model, tokenizer, config)
    return {
        "category": result["category_name"],  # Используем текстовое название
        "probability": round(result["probability"], 4)
    }


@app.get("/health")
async def health_check():
    return {"status": "healthy"}