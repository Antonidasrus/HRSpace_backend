# Generated by Django 3.2 on 2024-03-22 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_specialization_salary_recomend'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salaryrecomend',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_recomend', models.PositiveIntegerField(verbose_name='Рекомендуемая зарплата')),
            ],
            options={
                'verbose_name': 'Рекомендуемая зарплата',
                'verbose_name_plural': 'Рекомендуемые зарплаты',
            },
        ),
        migrations.RemoveField(
            model_name='specialization',
            name='salary_recomend',
        ),
        migrations.AlterField(
            model_name='specialization',
            name='skills_recomend',
            field=models.ManyToManyField(through='app.SkillSpecialization', to='app.Skill', verbose_name='Навыки специальности'),
        ),
        migrations.CreateModel(
            name='SalaryrecomendTown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_recomend', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.salaryrecomend', verbose_name='Рекомендуемые зарплаты по специальности')),
                ('specialization_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.specialization', verbose_name='Город')),
                ('town_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.towns', verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Рекомендуемые зарплаты по специальностям в городах',
                'verbose_name_plural': 'Рекомендуемые зарплаты по специальностям в городах',
                'ordering': ('specialization_id',),
            },
        ),
        migrations.AddField(
            model_name='specialization',
            name='salary_recomend',
            field=models.ManyToManyField(through='app.SalaryrecomendTown', to='app.Salaryrecomend', verbose_name='Зарплаты по специальностям в городах'),
        ),
    ]