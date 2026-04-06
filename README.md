# hello-python

Учебный Flask-проект. Включает форму приветствия и мини-анкету с REST API.

## Стек

- Python 3.12, Flask, Gunicorn
- HTML + Jinja2 + Vanilla JS
- Tailwind CSS (CDN)
- Docker

## Страницы

| Маршрут | Описание |
|---|---|
| `/` | Главная с формой приветствия |
| `/about` | О проекте |
| `/questionnaire` | Мини-анкета |

## API

| Метод | Маршрут | Описание |
|---|---|---|
| GET | `/api/questions` | Возвращает список вопросов (JSON) |
| POST | `/api/answers` | Принимает ответы на анкету (JSON) |

Ответы хранятся в памяти процесса (без базы данных).

## Локальный запуск

**Без Docker:**
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```
Приложение доступно на `http://127.0.0.1:5001`

**Через Docker:**
```bash
docker build -t hello-python .
docker run -p 8080:8080 hello-python
```
Приложение доступно на `http://localhost:8080`

## Сценарий использования

1. Открыть главную страницу `/`
2. Ввести имя — получить персональное приветствие
3. Перейти в раздел «Анкета» `/questionnaire`
4. Ответить на 5 вопросов и отправить форму
5. Получить подтверждение «Спасибо за ответы!»

## Использованные AI-промты

См. [PROMPTS.md](PROMPTS.md)
