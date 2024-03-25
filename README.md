# HRSpace_backend

[![CI](https://github.com/find-y/HRSpace_backend/actions/workflows/hrspace_workflow.yml/badge.svg?branch=feature/deploy)](https://github.com/find-y/HRSpace_backend/actions/workflows/hrspace_workflow.yml)

HRSpace - это API, разработанное специально для маркетплейса HRSpace с главной целью обновить и расширить возможности микросервис билдера заявки рекрутера. Наше API предлагает широкий спектр функций и инструментов, которые позволяют оптимизировать процесс создания заявок, делая его более гибким, эффективным и удобным

### `[Просмотр API](https://51.250.27.201/api/v1/)`

## Запуск проекта:
1. Клонируем проект.
```bash
git clone git@github.com:Antonidasrus/HRSpace_backend.git
```
2. Создаем и активируем виртуальное окружение. 
```bash
python -m venv venv
source venv/scripts/activate
```
3. Обновляем менеджер пакетов pip и устанавливаем зависимости из файла requirements.txt.
```bash
python -m pip install --upgrade pip
pip install -r api_yamdb/requirements.txt
```
4. Переходим в папку и создаем базу данных. 
```bash
cd api_yamdb
python manage.py migrate 
```
5. Запускаем проект.
```bash
python manage.py runserver 
```

## Запуск через контейнеры:
1. Переходим в папку и создаем файл.
```bash
cd infra
touch .env
```
2. Заходим в файл.
```bash
nano .env
```
3. Заполняем файл.
```conf
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=<свой пароль>
DB_HOST=db
DB_PORT=5432
```
4. Запускаем контейнеры.
```bash
docker-compose up -d
```
5. Создаем базу данных.
```bash
docker-compose exec backend python manage.py migrate
```
6. Собираем всю статику.
```bash
docker-compose exec backend python manage.py collectstatic --no-input
```

## Документация:
- ### [Swagger](https://51.250.27.201/api/v1/docs/Swagger)
- ### [Redoc](https://51.250.27.201/api/v1/docs/Redoc)

## Авторы:
| Имя | GitHub |
| - | :-: |
| Илья Василевсикй | <a href="https://github.com/IlyaVasilevsky47" target="_blank"> :heavy_check_mark:</a> |
| Яков Аустер | <a href="https://github.com/find-y" target="_blank"> :heavy_check_mark:</a> |
| Антон Коновалов | <a href="https://github.com/Antonidasrus" target="_blank"> :heavy_check_mark:</a> |

## Технический стек
- Python 3.10.0
- Django 3.2.16
- Django REST Framework 3.12.4
- Gunicorn 20.0.4
- django-cors-headers
- drf-yasg 1.21.7
- PostgreSQL
- Docker-compose
