# generator-citat
# Generator-C — генератор случайных цитат

Generator-C — учебный проект на Python, реализующий генератор случайных цитат.
Приложение поддерживает работу в режиме командной строки (CLI) и через веб-интерфейс на Flask.

Проект создан для практики:
- структуры Python-проекта
- работы с Flask
- использования Git и GitHub
- настройки CI (GitHub Actions)
- контроля качества кода с помощью flake8

---

## Функциональность

- вывод случайной цитаты в терминал (CLI-режим)
- веб-страница с кнопкой генерации новой цитаты
- API endpoint `/random`, возвращающий цитату в формате JSON
- автоматическая проверка кода при каждом push
- линтинг кода с помощью flake8

---

Структура проекта

<img width="285" height="201" alt="image" src="https://github.com/user-attachments/assets/7fa0c379-96b1-4bcd-8cf9-1012351abe35" />

generator-c/
├── quotes/
│ ├── api.py # Flask API и веб-интерфейс
│ ├── cli.py # CLI-интерфейс
│ ├── quote_service.py # Логика генерации цитат
│ ├── quotes.py # Список цитат
│ └── init.py
├── .github/
│ └── workflows/
│ └── ci.yml # CI (GitHub Actions)
├── main.py # Точка входа в приложение
├── requirements.txt # Зависимости проекта
└── README.md


---

Установка

Клонировать репозиторий:

```bash
git clone https://github.com/peersssona/generator-c.git
cd generator-c

---

## Установка

Клонировать репозиторий:

```bash
git clone https://github.com/peersssona/generator-c.git
cd generator-c
Создать виртуальное окружение:

python -m venv venv


Активировать виртуальное окружение (Windows):

venv\Scripts\activate


Установить зависимости:

pip install -r requirements.txt

Запуск проекта
CLI-режим

Выводит одну случайную цитату в терминал:

python main.py --mode cli

Web-режим

Запускает Flask-сервер:

python main.py --mode api


После запуска веб-интерфейс будет доступен по адресу:

http://127.0.0.1:5000

API
Получение случайной цитаты
GET /random


Пример ответа:

{
  "quote": "Жизнь — это путь, а не пункт назначения."
}

CI (Continuous Integration)

В проекте настроен CI с использованием GitHub Actions.

При каждом push в ветку main автоматически выполняется:

установка зависимостей

запуск линтера flake8

проверка стиля и базовых ошибок кода

Результаты проверок доступны во вкладке Actions репозитория.

Используемые технологии

Python

Flask

Git

GitHub

GitHub Actions

flake8

