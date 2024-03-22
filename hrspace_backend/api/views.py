from rest_framework.viewsets import ModelViewSet
from app.models import (Application,
                        Specialization,
                        Towns,
                        Language,
                        Skill,
                        Salaryrecomend)
from .serializers import (ApplicationSerializer,
                          SpecializationSerializer,
                          TownsSerializer,
                          LanguageSerializer,
                          SkillSerializer,
                          SalarySerializer,
                          AverageSalarySerializer
                          )
from .utils import istartswith_search
from rest_framework.response import Response



class SpecializationViewSet(ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


class TownsViewSet(ModelViewSet):
    queryset = Towns.objects.all()
    serializer_class = TownsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_name = self.request.query_params.get('specialization_name')
        # specialization_name = 'кодер'
        if specialization_name:
            queryset = queryset.filter(specialization__name=specialization_name)
        return istartswith_search(queryset, self)


class SalaryViewSet(ModelViewSet):
    queryset = Salaryrecomend.objects.all()
    serializer_class = SalarySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_name = self.request.query_params.get('specialization_name')
        # specialization_name = 'кодер'
        if specialization_name:
            queryset = queryset.filter(specialization__name=specialization_name)
        name = self.request.query_params.get('name')
        # name = 'Палк' # начало названия города
        if name:
            queryset = queryset.filter(salaryrecomendtown__town_id__name__istartswith=name)
        # print(queryset)
        # print('aaaaaaaaa')
        # if len(queryset)>1
        total_salary = sum(salary.salary_recomend for salary in queryset)
        average_salary = total_salary / queryset.count() if queryset.count() > 0 else 0
        # queryset = {'salary_recomend': average_salary}
        queryset = AverageSalarySerializer({'average_salary_recomend': average_salary})
        # return Response(serializer.data)
        return queryset


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
