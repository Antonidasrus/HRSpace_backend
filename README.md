# HRSpace_backend
## Backend for Hackaton project

## Заполненеие тестовыми данными БД:
1. Создаем базу дыннх.
```bash
python manage.py migrate
```
2. Заполняем тестовыми данными базу данных.
```bash
python manage.py load_data
```


## Stack:
### - Django, DRF, ORM (можно использовать FastAPI, но нам эта технология пока не знакома, поэтому не подходит)
### - Celery (для реализации асинхронности, по рекомендации наставника, идет в связке с Django)
### - Channels (для реализации чата)
### - CORS (политика для взаимодействия с фронтендом)
### - PostgreSQL (по рекомендации наставника, используется вместо SQLite)
### - Docker, Docker-compose
