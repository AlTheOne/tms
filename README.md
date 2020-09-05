# Тестовое задание Барс Груп

Создать систему ведения задач.

# Подготовка

Создаём контейнер:
```
$ docker-compose build
```

Создаём и накатываем миграции:
```
$ docker-compose run web python manage.py makemigrations
$ docker-compose run web python manage.py migrate
```

Запускаем процедуру создания Супер пользователя:
```
$ docker-compose run web python manage.py createsuperuser
```

# Запуск проект с помощью Docker

Запускаем приложение:
```
$ docker-compose up -d
```

Сайт доступен по адресу: `http://127.0.0.1:8000` 

*Внимание! Для удобства просмотра приложение запускается с DEV настройками.*