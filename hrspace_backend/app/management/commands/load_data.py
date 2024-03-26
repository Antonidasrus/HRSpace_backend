import io
import logging
from csv import DictReader

from django.core.management import BaseCommand
from tqdm import tqdm

from app.models import (Education, Expectations, Experience, Language,
                        LanguageLevel, Occupation, Payments, Registration,
                        Schedule, Skill, Towns)
from hrspace_backend.settings import BASE_DIR

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO
)

ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload the child data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""
MODELS_FIELD_NAME = (
    Towns,
    Experience,
    Education,
    Language,
    LanguageLevel,
    Registration,
    Occupation,
    Skill,
    Schedule,
    Expectations,
    Payments,
)


def application_app_models_fill():
    if Towns.objects.exists():
        logging.warning("Data already loaded...exiting.")
        raise Exception(ALREDY_LOADED_ERROR_MESSAGE)

    for index in range(len(MODELS_FIELD_NAME)):
        name_model = MODELS_FIELD_NAME[index].__name__
        logging.info(f"Loading - data a table - {name_model}")
        for row in tqdm(
            DictReader(
                io.open(f"{BASE_DIR}/static/data/{name_model}.csv", mode="r", encoding="utf-8")
            ),
            desc="Processing",
        ):
            MODELS_FIELD_NAME[index].objects.get_or_create(
                name=row["name"],
            )
        logging.info(f"Successfully - loading data table - {name_model}")
        logging.info("----------------------------------------")


class Command(BaseCommand):
    help = "Uploading test data to the database"

    def handle(self, *args, **options):
        logging.info("Downloading a model from the application app")
        logging.info("----------------------------------------")
        application_app_models_fill()
        logging.info("Successful loading of test data")
        return
