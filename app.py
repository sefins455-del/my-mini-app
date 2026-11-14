import random
import streamlit as st

# Настройка страницы
st.set_page_config(
    page_title="Mini App Generator", page_icon="⚡", layout="centered"
)

# Заголовок
st.title("⚡ Mini App Idea Generator")
st.write(
    "Нажмите на кнопку ниже, чтобы получить случайную идею для следующего мини-проекта!"
)

# Список идей
ideas = [
    {
        "title": "Кликкер с прокачкой талантов",
        "desc": "Игра на HTML5 Canvas с системой уровней и пассивным доходом.",
    },
    {
        "title": "Мини-блог в Telegram (Mini App)",
        "desc": "Приложение с профилем пользователя и лентой постов через FastAPI.",
    },
    {
        "title": "Генератор градиентов",
        "desc": "Инструмент для подбора красивых цветовых палитр с копированием CSS.",
    },
    {
        "title": "Погодный виджет",
        "desc": "Приложение с минималистичным интерфейсом и анимацией иконок.",
    },
]

# Кнопка генерации
if st.button("Сгенерировать идею! 🚀", type="primary"):
  chosen = random.choice(ideas)
  st.success(f"**{chosen['title']}**")
  st.info(chosen["desc"])

# Интерактивный слайдер для теста
st.divider()
st.subheader("Оцените сложность проекта:")
difficulty = st.slider("Уровень сложности (от 1 до 10)", 1, 10, 5)

if difficulty <= 3:
  st.write("🟢 Легкий старт — можно написать за пару часов.")
elif difficulty <= 7:
  st.yellow(
      "🟡 Средняя сложность — потребуется продумать логику и сохранение данных."
  )
else:
  st.write("🔴 Хардкор — полноценный проект на несколько дней разработки!")
