from django.db import models
# from django.db import models.Model

from users.models import User


class Profession(models.Model):
    name = models.TextField('Название профессии', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Профессия'
    #     verbose_name_plural = 'Профессии'
    #     ordering = ('-name',)

    # def __str__(self):
    #     return self.name


class Skill(models.Model):
    name = models.TextField('Название профессии', max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'Профессия'
    #     verbose_name_plural = 'Профессии'
    #     ordering = ('-name',)

    # def __str__(self):
    #     return self.name


class Application(models.Model):
    employer_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.TextField(
        verbose_name='Название вакансии'
    )
    # professions = models.ManyToManyField(
    #     Profession,
    #     through='ProfessionApplication',
    # )
    profession = models.ForeignKey(
        Profession,
        on_delete=models.CASCADE  #
    )
    skills = models.ManyToManyField(
        Skill,
        through='SkillApplication',
    )
    salary = models.PositiveIntegerField()
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


# class ProfessionApplication(models.Model):
#     application_id = models.ForeignKey(
#         Application,
#         on_delete=models.CASCADE
#     )
#     profession_id = models.ForeignKey(
#         Profession,
#         on_delete=models.CASCADE
#     )

class SkillApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    skill_id = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE
    )
