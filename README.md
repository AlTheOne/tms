# Тестовое задание Барс Груп

Система ведения задач.
- Нужно создать веб приложение на Django 2.2, Python 3.7.
- Верстка и внешний вид системы абсолютно не важны, фокус внимания на backend части.
- Исходники нужно обязательно выложить на github/gitlab/bitbucket.

Система осуществляет:
- поиск и учет задач;
- создание задач для определенных проектов;
- оповещение исполнителей об изменениях в задаче.
Система содержит сущности:
- Сотрудник (Имя, Проект, Email);
- Проект (Название);
- Задача (Важность, Исполнитель, Автор, Описание, Оценка времени на реализацию, Время затраченное на реализацию, Статус, Дата создания, Дата изменения); Задача в статусе «Реализовано» не должна редактироваться.
Такие сущности как Сотрудник / Проект заводятся в систему через админку.
Для доступа к главной странице требуется авторизоваться. На главной странице системы нужно отобразить список задач с возможностью поиска и создания новых. Должна быть возможность получить отчет о выполненных задачах по проектам за определенный период с указанием общего времени затраченного на их реализацию.

Бонусная секция(не обязательно к выполнению):
Запаковать проект в Docker образ

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

# Запуск проекта

Запускаем приложение:
```
$ docker-compose up -d
```

Сайт доступен по адресу: `http://127.0.0.1:8000` 

*Внимание! Для удобства просмотра приложение запускается с DEV настройками.*
