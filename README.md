Виртуальное окружение установлено (python virtualenv)

```python -m venv venv```

```source venv/bin/activate```

Сервисы, которые понадобятся для локальной разработки:
PostgreSQL 17.4

Перед началом работы, нужно установить все библиотеки

```pip install -r requirements.txt```

#### Применение миграция в проекте

```python manage.py migrate```

Если все ок идем дальше

#### Создание superuser

```python manage.py createsuper```

Указывает данные для superuser
Username: example
Email address: example@example.com
Password:
Password (again):

Если все ок, то напишет

Superuser created successfully.

После всего проделанного запускаем сервер

```python manage.py runserver```

Проверяем админку

```http://127.0.0.1:8000/admin```


