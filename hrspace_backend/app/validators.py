from django.utils import timezone
from django.core.exceptions import ValidationError


def date_validator(date):
    if date <= timezone.datetime.now().date() + timezone.timedelta(3):
        raise ValidationError(
            'Дата должна быть больше текущей даты на три дня'
        )
