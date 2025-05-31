import torch
from transformers import BertForSequenceClassification, BertTokenizer
import os


def load_model():
    model_path = "/app/production_model"
    print(f"Loading model from: {model_path}")
    print(f"Files in directory: {os.listdir(model_path)}")

    try:
        # Явно указываем использовать safetensors
        model = BertForSequenceClassification.from_pretrained(
            model_path,
            use_safetensors=True,
            local_files_only=True
        )
        tokenizer = BertTokenizer.from_pretrained(model_path)

        # Загрузка дополнительных данных
        additional_data = torch.load(
            os.path.join(model_path, 'additional_data.pth'),
            map_location='cpu'
        )

        return model, tokenizer, additional_data

    except Exception as e:
        print(f"Error loading model: {str(e)}")
        raise


def predict(text: str, model, tokenizer, config):
    inputs = tokenizer(
        text,
        max_length=config['max_len'],
        padding='max_length',
        truncation=True,
        return_tensors="pt"
    )
    with torch.no_grad():
        outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    pred_class = torch.argmax(probs).item()

    # Получаем ID категории (оригинальный, не перенумерованный)
    category_id = config['reverse_mapping'].get(pred_class, pred_class)

    # Получаем название категории
    category_name = config['category_names'].get(category_id, str(category_id))

    return {
        "category_id": category_id,  # Оставляем ID для внутреннего использования
        "category_name": category_name,  # Добавляем название категории
        "probability": probs[0][pred_class].item()
    }