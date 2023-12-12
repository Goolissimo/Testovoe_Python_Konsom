import streamlit as st
import requests

#API_URL = "http://.0.0.1:8000" для зауп
API_URL = "http://fastapi:8000"

st.title("Генерация одноразовых секретов")

action = st.selectbox("Выберите действие", ["Создать секрет", "Вернуть секрет по коду"])

if action == "Создать секрет":
    secret = st.text_input("Введите секрет")
    code_phrase = st.text_input("Введите кодовую фразу")
    if st.button("Создать"):
        response = requests.post(f"{API_URL}/generate", json={"secret": secret, "code_phrase": code_phrase})
        if response.status_code == 200:
            secret_key = response.json()["secret_key"]
            st.success(f"Ваш секретный ключ: {secret_key}", icon="✅")
        else:
            st.error("Не удалось создать секрет", icon="🚨")
elif action == "Вернуть секрет по коду":
    secret_key = st.text_input("Введите секретный ключ")
    if st.button("Вернуть секрет"):
        response = requests.post(f"{API_URL}/secrets/{secret_key}", json={"secret_key": secret_key})
        if response.status_code == 200:
            secret = response.json()["secret"]
            st.success(f"Ваш секрет: {secret}", icon="✅")
        else:
            st.error("Ошибка получения секрета", icon="🚨")