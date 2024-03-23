# Backend for HRSpace

## Команда:
- Антон - https://github.com/Antonidasrus
- Дмитрий - https://github.com/kda99
- Илья - https://github.com/IlyaVasilevsky47
- Яков - https://github.com/find-y

## Ссылка: https://51.250.27.201/api/v1/spaces/

## Инструкция по сборке и запуску:
1. Склонировать репозиторий к себе на компьютер:
```bash
git clone git@github.com:Antonidasrus/HRSpace_backend.git
```
2. Перейти в корневую папку проекта:
```bash
cd HRSpace_backend
```
3. Создать виртуальное окружение:
```bash
python -m venv venv
```
4. Активировать виртуальное окружение:
```bash
source venv/Scripts/activate
```
5. Установить зависимости:
```bash
pip install -r requirements.txt
```

## Заполнение тестовыми данными БД:
1. Обновляем виртуальное окружение, если не обновлено.
```bash
pip install -r requirements.txt
```
2. Создаем базу данных.
```bash
python manage.py migrate
```
3. Заполняем тестовыми данными базу данных.
```bash
python manage.py load_data
```

## Стек технологий:
- Django, DRF, ORM (можно использовать FastAPI, но нам эта технология пока не знакома, поэтому не подходит)
- Celery (для реализации асинхронности, по рекомендации наставника, идет в связке с Django)
- Channels (для реализации чата)
- CORS (политика для взаимодействия с фронтендом)
- PostgreSQL (по рекомендации наставника, используется вместо SQLite)
- Docker, Docker-compose

## Ссылки на сторонние фреймворки, библиотеки
