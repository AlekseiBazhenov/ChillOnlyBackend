Для установки зависимостей выполнить `pip install -r requirements.txt`

Запуск сервера `python manage.py runserver` 

При редактировании файла `models.py`, необходимо создать новую миграцию `python manage.py makemigrations`.
 
Затем необходимо применить командой `python manage.py migrate`, чтобы синхронизировать базы данных с моделями.