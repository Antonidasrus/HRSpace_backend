from django.db import models

from users.models import User


class TemplateName(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ('-name',)


class Specialization(TemplateName):
    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


class Towns(TemplateName):
    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'


class Experience(TemplateName):
    class Meta:
        verbose_name = 'Опыт работы в годах'
        verbose_name_plural = 'Варианты опыта работы в годах'


class Education(TemplateName):
    class Meta:
        verbose_name = 'Образование'
        verbose_name_plural = 'Варианты образования'


class Language(TemplateName):
    class Meta:
        verbose_name = 'Знание языка'
        verbose_name_plural = 'Знание языков'


class LanguageLevel(TemplateName):
    class Meta:
        verbose_name = 'Уровень языка'
        verbose_name_plural = 'Уровни языка'


class Registration(TemplateName):
    class Meta:
        verbose_name = 'Вариант оформления'
        verbose_name_plural = 'Варианты оформления'


class Occupation(TemplateName):
    class Meta:
        verbose_name = 'Тип занятости'
        verbose_name_plural = 'Типы занятости'


class Skill(TemplateName):
    class Meta:
        verbose_name = 'Навык'
        verbose_name_plural = 'Ключевые навыки'


class Schedule(TemplateName):
    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'Варианты графика работы'


class Expectations(TemplateName):
    class Meta:
        verbose_name = 'Задача рекрутера'
        verbose_name_plural = 'Задачи рекрутера'


class Payments(TemplateName):
    class Meta:
        verbose_name = 'Вариант выплаты рекрутеру'
        verbose_name_plural = 'Варианты выплат рекрутеру'


class Application(models.Model):
    # поля модели скомпанованы по типу:

    # данные проставляются автоматически
    employer_id = models.ForeignKey( ###
        User,
        on_delete=models.CASCADE,
    )
    date = models.DateField( ###
        auto_now_add=True,
        verbose_name='Дата публикации',
    )

    # юзер ставит галочку или нет
    mission = models.BooleanField() ### или поменять на выбор из нескольких?
    bonus = models.BooleanField() ###

    # юзер вводит значения вручную
    # name = models.TextField(
    #     default='Новая заявка', # на 2ом шаге данные подтягиваются из поле “специальность
    #     verbose_name='Название вакансии/заявки'
    # )
    salary = models.PositiveIntegerField() ###
    responsibilities = models.TextField(
        verbose_name='Обязанности'
    )
    # other_requirements = models.TextField(
    #     verbose_name='Прочие требования'
    # )
    countCandidates = models.PositiveIntegerField() ###
    countRecruiter = models.PositiveIntegerField() ###
    award = models.PositiveIntegerField() ###

    # юзер выбирает одно из списка. или добавляет свое
    specialization = models.ForeignKey( ###
        Specialization,
        on_delete=models.PROTECT,  # добавить: при вводе букв - подсказки
        verbose_name='Специальность',
    )
    towns = models.ForeignKey( ###
        Towns,
        on_delete=models.PROTECT,  # добавить: при вводе букв - подсказки
        verbose_name='Города',
    )
    experience = models.ForeignKey( ###
        Experience,
        on_delete=models.PROTECT,  # добавить: при вводе букв - подсказки
        verbose_name='Опыт работы',
    )
    education = models.ForeignKey( ###
        Education,
        on_delete=models.PROTECT,  # добавить: при вводе букв - подсказки
        verbose_name='Образование',
    )
    payments = models.ForeignKey( ###
        Payments,
        on_delete=models.PROTECT,  # добавить: при вводе букв появляются подсказки
        verbose_name='Варианты выплат рекрутеру',
    )


    # юзер выбирает несколько из списка
    skills = models.ManyToManyField(  ###
        Skill,
        through='SkillApplication',
        verbose_name='Навыки',
    )
    languages = models.ManyToManyField(  #### уточнить и переделать в несколько языков
        Language,
        through='LanguageApplication',
        verbose_name='Знание языков',
    )
    registration = models.ManyToManyField( ### чекчек
        Registration,
        through='RegistrationApplication',
        verbose_name='Варианты оформления',
    )
    occupation = models.ManyToManyField( ###
        Occupation,
        through='OccupationApplication',
        verbose_name='Тип занятости',
    )
    timetable = models.ManyToManyField(  ###
        Schedule,
        through='ScheduleApplication',
        verbose_name='График работы',
    )
    expectations = models.ManyToManyField(  ###
        Expectations,
        through='ExpectationsApplication',
        verbose_name='Задачи рекрутера',
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ('date',)

    def __str__(self):
        return self.specialization.name


class SkillApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE,
        verbose_name='Заявка'
    )
    skill_id = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
        verbose_name='Навык'
    )

    class Meta:
        verbose_name = 'Заявка-Навык'
        verbose_name_plural = 'Заявки-Навыки'
        ordering = ('application_id',)


class LanguageApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    language_id = models.ForeignKey(
        Language,
        on_delete=models.PROTECT
    )
    language_level = models.ForeignKey(
        LanguageLevel,
        on_delete=models.PROTECT  # добавить: при вводе букв появляются подсказки
    )


class ScheduleApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    Schedule_id = models.ForeignKey(
        Schedule,
        on_delete=models.PROTECT
    )


class OccupationApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    occupation_id = models.ForeignKey(
        Occupation,
        on_delete=models.PROTECT
    )


class RegistrationApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    registration_id = models.ForeignKey(
        Registration,
        on_delete=models.PROTECT
    )


class ExpectationsApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    expectations_id = models.ForeignKey(
        Expectations,
        on_delete=models.PROTECT
    )
