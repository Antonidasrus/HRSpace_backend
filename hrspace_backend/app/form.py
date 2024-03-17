# для теста в браузере до фронта

from django.forms import ModelForm

from .models import Application


class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = '__all__'
        # fields = ('name',)
