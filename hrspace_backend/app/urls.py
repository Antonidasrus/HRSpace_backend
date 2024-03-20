# для теста в браузере до фронта

from django.urls import include, path
from .views import index


urlpatterns = [
    path('', index)

]
