from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from users.models import User

BOOLEAN_CHOICES = ("Да", "Нет")
CANDIDATES_COUNT_CHOICES = [number for number in range(1, 11)]
RECRUITER_COUNT_CHOICES = [1, 2, 3]


class TemplateName(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ("-name",)


class Skill(TemplateName):
    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Ключевые навыки"


class Towns(TemplateName):
    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"


class Salaryrecomend(models.Model):
    salary_recomend = models.PositiveIntegerField("Рекомендуемая зарплата")

    def __str__(self):
        return str(self.salary_recomend)

    class Meta:
        verbose_name = "Рекомендуемая зарплата"
        verbose_name_plural = "Рекомендуемые зарплаты"


class Specialization(models.Model):
    name = models.CharField("Название", max_length=256, unique=True)
    skills_recomend = models.ManyToManyField(
        Skill,
        through="SkillSpecialization",
        verbose_name="Навыки специальности",
    )
    salary_recomend = models.ManyToManyField(
        Salaryrecomend,
        through="SalaryrecomendTown",
        verbose_name="Зарплаты по специальностям в городах",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Специальность"
        verbose_name_plural = "Специальности"


class SalaryrecomendTown(models.Model):
    town_id = models.ForeignKey(
        Towns, on_delete=models.CASCADE, verbose_name="Город"
    )
    specialization_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, verbose_name="Специльность"
    )
    salary_recomend = models.ForeignKey(
        Salaryrecomend,
        on_delete=models.PROTECT,
        verbose_name="Рекомендуемые зарплаты по специальности",
    )

    class Meta:
        verbose_name = "Рекомендуемые зарплаты по специальностям в городах"
        verbose_name_plural = "Рекомендуемые зарплаты по спец-тям в городах"
        ordering = ("specialization_id",)


class Experience(TemplateName):
    class Meta:
        verbose_name = "Опыт работы в годах"
        verbose_name_plural = "Варианты опыта работы в годах"


class Education(TemplateName):
    class Meta:
        verbose_name = "Образование"
        verbose_name_plural = "Варианты образования"


class Language(TemplateName):
    class Meta:
        verbose_name = "Знание языка"
        verbose_name_plural = "Знание языков"


class LanguageLevel(TemplateName):
    class Meta:
        verbose_name = "Уровень языка"
        verbose_name_plural = "Уровни языка"


class Registration(TemplateName):
    class Meta:
        verbose_name = "Вариант оформления"
        verbose_name_plural = "Варианты оформления"


class Occupation(TemplateName):
    class Meta:
        verbose_name = "Тип занятости"
        verbose_name_plural = "Типы занятости"


class Schedule(TemplateName):
    class Meta:
        verbose_name = "График работы"
        verbose_name_plural = "Варианты графика работы"


class Expectations(TemplateName):
    class Meta:
        verbose_name = "Задача рекрутера"
        verbose_name_plural = "Задачи рекрутера"


class Payments(TemplateName):
    class Meta:
        verbose_name = "Вариант выплаты рекрутеру"
        verbose_name_plural = "Варианты выплат рекрутеру"


class Application(models.Model):
    employer_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Работодатель",
    )
    date = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации",
    )
    mission = models.BooleanField(
        verbose_name="Командировки",
        null=True,
        blank=True,
    )
    bonus = models.BooleanField(
        verbose_name="Бонусы от работодателя",
        null=True,
        blank=True,
    )
    salary_min = models.PositiveBigIntegerField(
        verbose_name="Минимальная зарплата", null=True, blank=True
    )
    salary_max = models.PositiveBigIntegerField(
        verbose_name="Максимальня зараплта", null=True, blank=True
    )
    responsibilities = models.TextField(verbose_name="Обязанности сотрудника")
    other_requirements = models.TextField(
        verbose_name="Дополнительные требования", blank=True
    )
    candidates_count = models.PositiveSmallIntegerField(
        verbose_name="Количество кандидатов",
        validators=[
            MinValueValidator(CANDIDATES_COUNT_CHOICES[0]),
            MaxValueValidator(CANDIDATES_COUNT_CHOICES[-1]),
        ],
    )
    recruiter_count = models.PositiveSmallIntegerField(
        verbose_name="Количество рекрутеров",
        validators=[
            MinValueValidator(RECRUITER_COUNT_CHOICES[0]),
            MaxValueValidator(RECRUITER_COUNT_CHOICES[-1]),
        ],
    )
    award = models.PositiveIntegerField(
        verbose_name="Вознаграждение рекрутера"
    )
    name = models.CharField(
        default="Новая заявка",
        max_length=256,
        verbose_name="Название вакансии/заявки"
    )
    specialization = models.ForeignKey(
        Specialization,
        on_delete=models.PROTECT,
        verbose_name="Специальность",
    )
    towns = models.ForeignKey(
        Towns,
        on_delete=models.PROTECT,
        verbose_name="Города",
    )
    experience = models.ForeignKey(
        Experience,
        on_delete=models.PROTECT,
        verbose_name="Опыт работы",
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.PROTECT,
        verbose_name="Образование",
    )
    payments = models.ForeignKey(
        Payments,
        on_delete=models.PROTECT,
        verbose_name="Варианты выплат рекрутеру",
    )
    skills = models.ManyToManyField(
        Skill,
        through="SkillApplication",
        verbose_name="Навыки",
    )
    languages = models.ManyToManyField(
        Language,
        through="LanguageApplication",
        verbose_name="Знание языков",
        blank=True,
    )
    registration = models.ManyToManyField(
        Registration,
        through="RegistrationApplication",
        verbose_name="Варианты оформления",
    )
    occupation = models.ManyToManyField(
        Occupation,
        through="OccupationApplication",
        verbose_name="Тип занятости",
    )
    timetable = models.ManyToManyField(
        Schedule,
        through="ScheduleApplication",
        verbose_name="График работы",
    )
    expectations = models.ManyToManyField(
        Expectations,
        through="ExpectationsApplication",
        verbose_name="Задачи рекрутера",
    )

    # def clean(self):
    #     if not self.salary_min and not self.salary_max:
    #         raise ValidationError({
    #             "salary_max": (
    #                 "Пожалуйста, заполните salary_min или salary_max"
    #             ),
    #             "salary_min": (
    #                 "Пожалуйста, заполните salary_min или salary_max"
    #             ),
    #         })
    #     if self.salary_min and self.salary_max:
    #         if self.salary_min > self.salary_max:
    #             raise ValidationError({
    #                 "salary_min": (
    #                     "Минимальная зарплата"
    #                     "не может быть больше максимальной"
    #                 )
    #             })

    def __str__(self):
        return self.specialization.name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ("date",)


class SkillApplication(models.Model):
    application_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, verbose_name="Заявка"
    )
    skill_id = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
        verbose_name="Навык"
    )

    class Meta:
        verbose_name = "Заявка-Навык"
        verbose_name_plural = "Заявки-Навыки"
        ordering = ("application_id",)


class LanguageApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        related_name="language_list",
        verbose_name="Заявка",
    )
    language_id = models.ForeignKey(
        Language,
        on_delete=models.PROTECT,
        related_name="language_list",
        verbose_name="Язык",
    )
    language_level = models.ForeignKey(
        LanguageLevel,
        on_delete=models.PROTECT,
        verbose_name="Уровень языка",
    )

    class Meta:
        verbose_name = "Заявка-Язык"
        verbose_name_plural = "Заявки-Языки"
        ordering = ("application_id",)


class ScheduleApplication(models.Model):
    application_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, verbose_name="Заявка"
    )
    Schedule_id = models.ForeignKey(
        Schedule, on_delete=models.PROTECT, verbose_name="График"
    )

    class Meta:
        verbose_name = "Заявка-График"
        verbose_name_plural = "Заявка-Графики"
        ordering = ("application_id",)


class OccupationApplication(models.Model):
    application_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, verbose_name="Заявка"
    )
    occupation_id = models.ForeignKey(
        Occupation, on_delete=models.PROTECT, verbose_name="ТипЗанятости"
    )

    class Meta:
        verbose_name = "Заявка-ТипЗанятости"
        verbose_name_plural = "Заявка-ТипыЗанятости"
        ordering = ("application_id",)


class RegistrationApplication(models.Model):
    application_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, verbose_name="Заявка"
    )
    registration_id = models.ForeignKey(
        Registration, on_delete=models.PROTECT, verbose_name="Оформление"
    )

    class Meta:
        verbose_name = "Заявка-Оформление"
        verbose_name_plural = "Заявка-Оформление"
        ordering = ("application_id",)


class ExpectationsApplication(models.Model):
    application_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, verbose_name="Заявка"
    )
    expectations_id = models.ForeignKey(
        Expectations, on_delete=models.PROTECT, verbose_name="ЗадачаРекрутера"
    )

    class Meta:
        verbose_name = "Заявка-ЗадачаРекрутера"
        verbose_name_plural = "Заявка-ЗадачиРекрутера"
        ordering = ("application_id",)


class SkillSpecialization(models.Model):
    specialization_id = models.ForeignKey(
        Specialization, on_delete=models.CASCADE, verbose_name="Специальность"
    )
    skill_id = models.ForeignKey(
        Skill, on_delete=models.PROTECT, verbose_name="Навык"
    )

    class Meta:
        verbose_name = "Специальность-Навык"
        verbose_name_plural = "Специальности-Навыки"
        ordering = ("specialization_id",)
