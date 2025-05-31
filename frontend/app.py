import streamlit as st
import requests

st.set_page_config(page_title="Классификатор запросов")

st.title("🛍️ Классификация товарных запросов")
st.write("Определение категории товара по тексту запроса")

text_input = st.text_area("Введите текст запроса:", height=100)

if st.button("Определить категорию"):
    if text_input.strip():
        try:
            response = requests.post(
                "http://backend:8000/predict",
                json={"text": text_input}
            )
            if response.status_code == 200:
                result = response.json()
                st.success(
                    f"**Категория:** {result['category']}\n\n"
                    f"**Вероятность:** {result['probability']*100:.1f}%"
                )
            else:
                st.error("Ошибка при обработке запроса")
        except Exception as e:
            st.error(f"Ошибка соединения с сервером: {str(e)}")
    else:
        st.warning("Введите текст для классификации")