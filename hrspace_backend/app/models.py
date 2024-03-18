from django.core.validators import MinValueValidator
from django.db import models


class TemplateName(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=200
    )

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        abstract = True
        ordering = ('id', )


class Profession(TemplateName):
    class Meta:
        verbose_name = 'Профессия'
        verbose_name_plural = 'Профессии'


class Duty(TemplateName):
    class Meta:
        verbose_name = 'Обязанность'
        verbose_name_plural = 'Обязанности'


class Claim(TemplateName):
    class Meta:
        verbose_name = 'Требование'
        verbose_name_plural = 'Требования'


class Skill(TemplateName):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Навыки'


class Other(TemplateName):
    class Meta:
        verbose_name = 'Прочие'
        verbose_name_plural = 'Прочие'


class Citizenship(TemplateName):
    class Meta:
        verbose_name = 'Гражданство'
        verbose_name_plural = 'Гражданство'


class Application(models.Model):
    name = models.CharField(
        verbose_name='Название', max_length=200
    )
    # employer_id = ...
    profession_id = models.ManyToManyField(
        Profession,
        through='ApplicationProfession',
        related_name='profession_application',
        verbose_name='Профессия'
    )
    salary_min = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1)
        ],
        verbose_name='Минимальная з/п'
    )
    salary_max = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1)
        ],
        verbose_name='Максимальная з/п'
    )
    description_duties = models.ManyToManyField(
        Duty,
        through='ApplicationDuty',
        related_name='duties_application',
        verbose_name='описание обязанностей'
    )
    description_claims = models.ManyToManyField(
        Claim,
        through='ApplicationClaim',
        related_name='claims_application',
        verbose_name='Описание требований'
    )
    description_skills = models.ManyToManyField(
        Skill,
        through='ApplicationSkill',
        related_name='skills_application',
        verbose_name='Описание навыков'
    )
    description_other = models.ManyToManyField(
        Other,
        through='ApplicationOther',
        related_name='other_application',
        verbose_name='Прочие описание'
    )
    citizenship_id = models.ManyToManyField(
        Citizenship,
        through='ApplicationCitizenship',
        related_name='citizenship_application',
        verbose_name='Гражданство'
    )
    # city = models.ForeignKey()
    # experience = ...
    # education = ...
    # language_level = ...
    # driving_license = ... # (boolean)
    # extra_info = ...
    # employment_mode = ...
    # work_registration = ...
    # work_place = ...
    # business_trips = ... # (boolean)
    # bonuses = ...
    # Application_hr_id = ...


class ApplicationProfession(models.Model):
    application = models.ForeignKey(
        Application,
        # related_name='applications_id',
        on_delete=models.CASCADE,
        verbose_name='Заявка',
    )
    profession = models.ForeignKey(
        Profession,
        related_name='professions_id',
        on_delete=models.CASCADE,
        verbose_name='Профессия',
    )

    class Meta:
        verbose_name = 'ЗаявкаПрофессия'
        verbose_name_plural = 'ЗаявкаПрофессия'


class ApplicationDuty(models.Model):
    application = models.ForeignKey(
        Application,
        # related_name='applications_id',
        on_delete=models.CASCADE,
        verbose_name='Заявка',
    )
    duty = models.ForeignKey(
        Duty,
        # related_name='',
        on_delete=models.CASCADE,
        verbose_name='Обязанность',
    )

    class Meta:
        verbose_name = 'ЗаявкаОбязанности'
        verbose_name_plural = 'ЗаявкаОбязанности'


class ApplicationClaim(models.Model):
    application = models.ForeignKey(
        Application,
        # related_name='applications_id',
        on_delete=models.CASCADE,
        verbose_name='Заявка',
    )
    claim = models.ForeignKey(
        Claim,
        # related_name='',
        on_delete=models.CASCADE,
        verbose_name='Требования',
    )

    class Meta:
        verbose_name = 'ЗаявкаТребования'
        verbose_name_plural = 'ЗаявкаТребования'


class ApplicationSkill(models.Model):
    application = models.ForeignKey(
        Application,
        # related_name='applications_id',
        on_delete=models.CASCADE,
        verbose_name='Заявка',
    )
    skill = models.ForeignKey(
        Skill,
        # related_name='',
        on_delete=models.CASCADE,
        verbose_name='Навыки',
    )

    class Meta:
        verbose_name = 'ЗаявкаНавыки'
        verbose_name_plural = 'ЗаявкаНавыки'


class ApplicationOther(models.Model):
    application = models.ForeignKey(
        Application,
        # related_name='applications_id',
        on_delete=models.CASCADE,
        verbose_name='Заявка',
    )
    other = models.ForeignKey(
        Other,
        # related_name='',
        on_delete=models.CASCADE,
        verbose_name='Прочие',
    )

    class Meta:
        verbose_name = 'ЗаявкаПрочие'
        verbose_name_plural = 'ЗаявкаПрочие'


class ApplicationCitizenship(models.Model):
    application = models.ForeignKey(
        Application,
        # related_name='applications_id',
        on_delete=models.CASCADE,
        verbose_name='Заявка',
    )
    сitizenship = models.ForeignKey(
        Citizenship,
        # related_name='',
        on_delete=models.CASCADE,
        verbose_name='Прочие',
    )

    class Meta:
        verbose_name = 'ЗаявкаГражданство'
        verbose_name_plural = 'ЗаявкаГражданство'
