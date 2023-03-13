# Сервис уведомлений

Приложение разработано на фреймворке django rest_framework

Технические требования дли второй части ТЗ
* Django 4.1.7, DRF 3.14.0
* PostgreSQL 13
* Python 3.9.5
* aiohttp 3.8.4
* PyDantic 1.10.6

## Инструкция по настройке проекта:

1. Клонировать проект
```bash
git clone https://github.com/SergeySelya/api_wildberries.git
```

2. Открыть проект в PyCharm с наcтройками по умолчанию
3. Создать виртуальное окружение (через settings -> project "api_wildberries" -> project interpreter)
4. Открыть терминал в PyCharm, проверить, что виртуальное окружение активировано.
5. Обновить pip:
   ```bash
   pip install --upgrade pip
   ```
6. Установить в виртуальное окружение необходимые пакеты: 
   ```bash
   pip install --default-timeout=100 -r requirements.txt
   ```
7. Настроить подключение к БД (PostgresSQL13) в api_wildberries\config\settings.py 
![img_1.png](img_1.png)
8. Синхронизировать структуру базы данных с моделями: 
   ```bash
   python manage.py migrate
   ```

10. Запускаем приложение в в PyCharm (файл `manage.py`, опция `runserver`)
python manage.py runserver

## Список api:
1. http://127.0.0.1:8000/api/product_info_wb/upload/


