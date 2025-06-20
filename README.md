<img src="picturies/logo.png" alt="Irene Atelier Logo" width="200" align="right">

# 🌟 Irene Atelier Bot

**Telegram-бот для ювелирного дома "Irene Atelier"**  
Упрощенное взаимодействие между клиентами и ювелирной мастерской

---

## 📌 О проекте
Бот предоставляет клиентам удобный интерфейс для:
- Создания референсов новых ювелирных украшений
- Оформления заявок на ремонт существующих изделий
- Быстрой коммуникации с мастерами

---

## 🏗 Структура проекта 
## Структура проекта:
```text
├── handlers/                  # Обработчики команд и событий
│   ├── atelier_handlers.py    # Ремонт украшений
│   ├── commands.py            # Системные команды (/start, /help)
│   └── create_jew_handlers.py # Создание новых украшений
├── picturies/                 # Медиа-файлы
├── config.py                  # Конфигурация (токен бота)
├── kb.py                      # Клавиатуры (статич. и динамич.)
├── main.py                    # Точка входа
├── states.py                  # FSM и Callback Data
└── text.py                    # Текстовые ресурсы
```

## 🛠 Технологии
<p>
  <img src="https://img.shields.io/badge/Python-3.9+-blue?logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Aiogram-3.x-blue?logo=telegram" alt="Aiogram">
</p>

---

## 🚀 Установка
1. Клонировать репозиторий:
   ```bash
   git clone https://github.com/yourusername/irene-atelier-bot.git
   cd irene-atelier-bot
   ```
2. Настроить окружение:
   ```bash
   python -m venv .venv
   ```
   ```bash
   source venv/bin/activate  # Linux/Mac
   ```
   ```bash
   venv\Scripts\activate     # Windows
   ```
3. Установить зависимости:
   ```bash
   pip install -r requirements.txt 
   ```
4. Запустить бота:
   ```bash
   python main.py 
   ```

## Демонстрация

📸 Демонстрация интерфейса
<div align="center">
  <table>
    <tr> 
      <td align="center"> <img src="img_for_github/start.PNG" width="300"></td> 
      <td align="center"> <img src="img_for_github/choice_1.PNG" width="300"></td> 
    </tr> 
    <tr> 
      <td align="center"> <img src="img_for_github/choice_2.PNG" width="300"></td>
      <td align="center"> <img src="img_for_github/choice_3.PNG" width="300"></td>
    </tr> 
  </table> 
</div>
