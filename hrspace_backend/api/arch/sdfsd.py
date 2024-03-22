from django.db import models


class Skill(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)

    def __str__(self):
        return self.name


class Specialization(models.Model):
    name = models.CharField('Название', max_length=256, unique=True)
    skills = models.ManyToManyField(
        Skill,
        through='SkillSpecialization',
    )

    def __str__(self):
        return self.name


class SkillSpecialization(models.Model):
    specialization_id = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
    )
    skill_id = models.ForeignKey(
        Skill,
        on_delete=models.PROTECT,
    )
