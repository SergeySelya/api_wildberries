Author: Селивончик С.В.  
*   Task1:\api_wildberries\Task1\user_connect.py
*   Task2:
# Сервис получения данных о товаре с Wildberries

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
![image](https://user-images.githubusercontent.com/88445455/224683654-7f106c66-d4e8-4db5-aeba-8c2477891201.png)
8. Синхронизировать структуру базы данных с моделями: 
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
10. Запускаем приложение в в PyCharm (файл `manage.py`, опция `runserver`)
python manage.py runserver

## API возвращающий данные о карточке товара:
1. http://127.0.0.1:8000/api/product_info_wb/upload/

После запуска приложения открываем Postman:
1) указываем URl "http://127.0.0.1:8000/api/product_info_wb/upload/"
2) выбираем метод POST
3) В поле form-data прописываем параметр для передачи данных (KEY: 'file'), выбираем выбираем text или file и прикрепляем данные запросу.
Пример отправки запроса:
![image](https://user-images.githubusercontent.com/88445455/224682803-fdb201bd-1e77-4994-ab87-c5f8d488f6b0.png)




