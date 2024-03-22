# заготовка, чтобы вынести часть для рекрутера в отдельное приложение


'''
from django.db import models
from app.models import Application


class Wait(models.Model):
    name = models.TextField(max_length=256, unique=True)

    # class Meta:
    #     verbose_name = 'непонятно'
    #     ordering = ('-name',)

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
        Wait,
        through='WaitApplication',
    )


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.name


class WaitApplication(models.Model):
    application_id = models.ForeignKey(
        Application,
        on_delete=models.CASCADE
    )
    bonus_id = models.ForeignKey(
        Bonus,
        on_delete=models.CASCADE
    )
'''
