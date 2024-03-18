from django.shortcuts import render
from .form import ApplicationForm


# для теста в браузере до фронта
def index(request): 
    form = ApplicationForm(request.POST or None)
    if not form.is_valid():
        return render(request, 'hrspace/base.html', {'form': form})
    # name = form.save(commit=False)
    # name.save
    return render(request, 'hrspace/base.html', {'form': form})
