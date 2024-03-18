from django.db import models
# from django.db import models.Model

from users.models import User


class Profession(models.Model):
    name = models.TextField('Название профессии', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Профессия'
    #     verbose_name_plural = 'Профессии'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Город'
    #     verbose_name_plural = 'Города'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Experience(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Опыт работы'
    #     verbose_name_plural = 'Варианты опыта работы'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Education(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Образование'
    #     verbose_name_plural = 'Варианты образования'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Знание языка'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class LanguageLevel(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Уровень языка'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Bonus(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Бонус'
    # verbose_name_plural = 'Бонусы'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Registration(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Уровень языка'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.TextField('Название профессии', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Профессия'
    #     verbose_name_plural = 'Профессии'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Schedule(models.Model):
    name = models.TextField('График работы', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'График работы'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Wait(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'непонятно'
    #     ordering = ('-name',)

    def __str__(self):
        return self.name


class Application(models.Model):
    # проставляется автоматически
    employer_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created = models.DateField(auto_now_add=True)

    # ставит галочку или нет
    trips = models.BooleanField() # или поменять на выбор из нескольких?
    has_bonuses = models.BooleanField()

    # поля, в которые юзер вводит значения вручную
    name = models.TextField(
        default='Новая заявка', # на 2ом шаге данные подтягиваются из поле “специальность
        verbose_name='Название вакансии/заявки'
    )
    salary = models.PositiveIntegerField()
    responsibilities = models.TextField(
        verbose_name='Обязанности'
    )
    other_requirements = models.TextField(
        verbose_name='Прочие требования'
    )

    # юзер выбирает одно из списка. или добавляет свое
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE  # при вводе букв появляются подсказки
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE  # при вводе букв появляются подсказки
    )
    experience = models.ForeignKey(
        Experience,
        on_delete=models.CASCADE  # при вводе букв появляются подсказки
    )
    education = models.ForeignKey(
        Education,
        on_delete=models.CASCADE  # при вводе букв появляются подсказки
    )
    foreign_language = models.ForeignKey(  #### уточнить и переделать в несколько языков
        Language,
        on_delete=models.CASCADE  # при вводе букв появляются подсказки
    )
    language_level = models.ForeignKey(
        LanguageLevel,
        on_delete=models.CASCADE  # при вводе букв появляются подсказки
    )


    # юзер выбирает несколько из списка
    skills = models.ManyToManyField(
        Skill,
        through='SkillApplication',
    )
    registration = models.ManyToManyField(
        Registration,
        through='RegistrationApplication',
    )
    schedule = models.ManyToManyField(
        Schedule,
        through='ScheduleApplication',
    )
    bonuses = models.ManyToManyField(
        Bonus,
        through='BonusApplication',
    )

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


# пока добавил одно поля дня теста
class Application_hr(models.Model):
    # проставляется автоматически
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    created = models.DateField(auto_now_add=True)

    # ставит галочку или нет

    # поля, в которые юзер вводит значения вручную

    # юзер выбирает одно из списка. или добавляет свое

    # юзер выбирает несколько из списка
    wait = models.ManyToManyField(  # жду ответ, о чем это поле
        Skill,
        through='WaitApplication',
    )


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name    


class SkillApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    skill_id = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )


class ScheduleApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    Schedule_id = models.ForeignKey(
        Schedule,
        on_delete=models.CASCADE
    )


class RegistrationApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    registration_id = models.ForeignKey(
        Registration,
        on_delete=models.CASCADE
    )


class BonusApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    bonus_id = models.ForeignKey(
        Bonus,
        on_delete=models.CASCADE
    )


class WaitApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    bonus_id = models.ForeignKey(
        Bonus,
        on_delete=models.CASCADE
    )
