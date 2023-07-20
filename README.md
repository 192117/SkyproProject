# REST API для Skypro

[Тестовое задание](https://docs.google.com/document/d/1AvlDF9SM8PSZq-lO9aDcXyP4LaMyuxYOd_HHc3kwKHQ/edit?usp=sharing)

## Установка

Перед началом установки убедитесь, что у вас установлен Python 3.11 и Poetry (пакетный менеджер для Python).

1. Склонируйте репозиторий:

`git clone https://github.com/192117/SkyproProject.git`

2. Перейдите в директорию:

`cd SkyproProject`

## Запуск приложения без Docker Compose (после пункта "Установка")

1. Установите зависимости с помощью Poetry:

`poetry install`

2. Создайте переменные окружения:

_Создайте файл .env на основе .env_example для запуска без Docker и файл .env.docker на основе .env_example для 
запуска с Docker. Оба файла содержат переменные окружения, которые требуются для настройки приложения._

3. Примените ДАМП на базу:

`psql -h HOST -p PORT -U USER -d DATABASE < my_dump.sql`

4. Запустите приложеие с помощью Poetry:

`poetry run uvicorn app:app --host 0.0.0.0 --port 8000`

5. Кредо:

Теперь у Вас есть **superuser** c данными (логин: admin, пароль: admin) и **user** c данными 
(логин: test_user, пароль: pQZV+3d2WfEHhE2)

6. Доступ к приложению: 

- [Документация swagger](http://127.0.0.1:8000/api/schema/swagger)
- [Документация redoc](http://127.0.0.1:8000/api/schema/redoc)


## Запуск приложения c использованием Docker Compose (после пункта "Установка")

1. Создайте переменные окружения:

_Создайте файл .env на основе .env_example для запуска без Docker и файл .env.docker на основе .env_example для 
запуска с Docker. Оба файла содержат переменные окружения, которые требуются для настройки приложения._

2. Запустите сборку docker-compose:

`docker compose up -d --build`

3. Кредо:

Теперь у Вас есть **superuser** c данными (логин: admin, пароль: admin) и **user** c данными 
(логин: test_user, пароль: pQZV+3d2WfEHhE2)

4. Доступ к приложению: 

- [Документация swagger](http://127.0.0.1:8888/api/schema/swagger)
- [Документация redoc](http://127.0.0.1:8888/api/schema/swagger)

## Запуск тестов

`poetry run test`

