# my_django_course

Закончил 4.4  
Закончил 3.12
Закончил 3.8
Закончил 3.7
Закончил 3.6
Закончил 3.5
Закончил 3.4
Закончил 3.3
Закончил 3.2
Закончил 3.1
Закончил 2.13   
Закончил 2.12
Закончил 2.8
Закончил 2.7
Закончил 2.5
Закончил 2.3
Закончил 1.7

https://stepik.org/lesson/681498/step/1?unit=680277


BD

manage.py makemigrations
manage.py migration



pip install Django - установка django

pip freeze - проверить что установлено

django-admin startproject myproject   - создать новый проект (генерирует структуру)

python manage.py runserver            - запустить тестовый сервер (на http://127.0.0.1:8000)

python manage.py runserver 0.0.0.0:80 - запустить тестовый сервер доступный извне (не 
                                        злоупотреблять)

django-admin startapp myapp           - создать приложение в текущем проекте

django-admin makemessages             - сгенерировать файлы с сообщениями подлежащими локализации

django-admin compilemessages          - скомпилировать файлы локализации

python manage.py makemigrations       - создать файлы миграций для БД

python manage.py sqlmigrate app 0001  - просмотр sql-кода, сгенерированного в миграции 0001 
                                        приложения app

python manage.py shell                - запустить окно командной строки

python manage.py test                 - прогнать тесты (для прогона будет создана чистая БД)

python manage.py test --verbosity=2   - управление детализацией вывода при тестах (2-макс, 0 - мин)

python manage.py createsuperuser      - создать пользователя-администратора