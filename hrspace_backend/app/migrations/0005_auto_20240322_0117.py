# Generated by Django 3.2 on 2024-03-21 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20240321_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='specialization',
            name='salary_recomend',
            field=models.PositiveIntegerField(default=1, verbose_name='Зарплата'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specialization',
            name='skills_recomend',
            field=models.ManyToManyField(through='app.SkillSpecialization', to='app.Skill', verbose_name='Навыки'),
        ),
    ]
