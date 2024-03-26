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


class Language(TemplateName):
    class Meta:
        verbose_name = "Знание языка"
        verbose_name_plural = "Знание языков"


class LanguageLevel(TemplateName):
    class Meta:
        verbose_name = "Уровень языка"
        verbose_name_plural = "Уровни языка"


class Application(models.Model):

    # юзер ставит галочку или нет
    bonus = models.BooleanField(verbose_name="Бонусы от работодателя", null=True)

    # юзер вводит значения вручную
    salary_min = models.PositiveBigIntegerField(
        verbose_name="Минимальная зарплата", blank=True
    )

    # юзер выбирает одно из списка. или добавляет свое

    towns = models.ForeignKey(
        Towns,
        on_delete=models.PROTECT,
        verbose_name="Города",
    )

    # юзер выбирает несколько из списка
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

    def __str__(self):
        return self.specialization.name


class SkillApplication(models.Model):
    application_id = models.ForeignKey(
        Application, on_delete=models.CASCADE, verbose_name="Заявка"
    )
    skill_id = models.ForeignKey(Skill, on_delete=models.PROTECT, verbose_name="Навык")


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
        on_delete=models.PROTECT,  # добавить: при вводе букв - подсказки
        verbose_name="Уровень языка",
    )
