# HRSpace_backend
## Backend for Hackaton project

## Stack:
### - Django, DRF, ORM (можно использовать FastAPI, но нам эта технология пока не знакома, поэтому не подходит)
### - Celery (для реализации асинхронности, по рекомендации наставника, идет в связке с Django)
### - Channels (для реализации чата)
### - CORS (политика для взаимодействия с фронтендом)
### - PostgreSQL (по рекомендации наставника, используется вместо SQLite)
### - Docker, Docker-compose


Запуск проекта локально

1. Выполнить по очереди команды
git clone git@github.com:Antonidasrus/HRSpace_backend.git
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

2. Добавить тестовые данные
POST-запрос на: http://127.0.0.1:8000/api/v1/spaces/

{
    "mission": true,
    "bonus": false,
    "salary_min": 50,
    "salary_max": 100,
    "responsibilities": "печь пирожки",
    "other_requirements": "other_requirements",
    "candidates_count": 2,
    "recruiter_count": 2,
    "award": 50000,
    "name": "плотник",
    "employer_id": 1,
    "specialization": 1,
    "towns": 1,
    "experience": 2,
    "education": 1,
    "payments": 1,
    "skills": [],
    "languages": [],
    "registration": [],
    "occupation": [],
    "timetable": [],
    "expectations": []
}
