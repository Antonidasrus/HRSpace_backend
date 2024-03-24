from rest_framework.viewsets import ModelViewSet
from datetime import datetime
from rest_framework.views import APIView
from app.models import (Application,
                        Specialization,
                        Towns,
                        Language,
                        Skill,
                        Salaryrecomend,
                        LanguageLevel,
                        Experience,
                        Education,
                        Payments,
                        Towns,
                        Language,
                        Registration,
                        Schedule,
                        Occupation,
                        Expectations,
                        BonusChoices,
                        MissionChoices,
                        CANDIDATES_COUNT_CHOICES,
                        RECRUITER_COUNT_CHOICES)
from .serializers import (SpecializationSerializer,
                          ApplicationSerializer,
                          TownsSerializer,
                          LanguageSerializer,
                          SkillSerializer,
                          SalarySerializer,
                          )
from .utils import istartswith_search
from rest_framework.response import Response
from django.db.models import Avg
# from rest_framework.response import Response
# from rest_framework import status


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
        specialization_name = self.request.query_params.get(
            'specialization_name')
        # specialization_name = 'кодер'
        if specialization_name:
            queryset = queryset.filter(
                specialization__name=specialization_name)
        return istartswith_search(queryset, self)


class SalaryViewSet(ModelViewSet):
    queryset = Salaryrecomend.objects.all()
    serializer_class = SalarySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_name = self.request.query_params.get(
            'specialization_name')
        # specialization_name = 'кодер'
        if specialization_name:
            queryset = queryset.filter(
                specialization__name=specialization_name)
        name = self.request.query_params.get('name')
        # name = 'Палк' # начало названия города
        if name:
            queryset = queryset.filter(
                salaryrecomendtown__town_id__name__istartswith=name)
        average_salary = queryset.aggregate(average_salary=Avg(
            'salary_recomend'))['average_salary']
        created_salary_recomend = Salaryrecomend(
            salary_recomend=average_salary)
        return [created_salary_recomend]
# проверить, что попсле выбора города,
# берет данные по нему, и уже не использует istartswith


class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    # def perform_create(self, serializer):
    #     if 'drafts' in self.request.path:
    #         appstatus_id = 'draft'
    #     else:
    #         appstatus_id = 'active'

    #     # Добавляем appstatus в данные перед сохранением объекта
    #     serializer.save(appstatus_id=appstatus_id)

    # # Метод для возврата корректного статуса HTTP в случае успеха
    # def create(self, request, *args, **kwargs):
    #     response = super().create(request, *args, **kwargs)
    #     if response.status_code == status.HTTP_201_CREATED:
    #         return Response(
    # {'status': 'success'}, status=status.HTTP_201_CREATED)
    #     return response


class AllData(APIView):
    def get(self, request):
        skills_list = list(Skill.objects.values_list('name', flat=True))
        specialization_list = list(Specialization.objects.values_list('name', flat=True))
        experience_list = list(Experience.objects.values_list('name', flat=True))
        education_list = list(Education.objects.values_list('name', flat=True))
        payments_list = list(Payments.objects.values_list('name', flat=True))
        towns_list = list(Towns.objects.values_list('name', flat=True))
        languages_list = list(Language.objects.values_list('name', flat=True))
        languages_levels_list = list(LanguageLevel.objects.values_list('name', flat=True))
        registration_list = list(Registration.objects.values_list('name', flat=True))
        occupation_list = list(Occupation.objects.values_list('name', flat=True))
        timetable_list = list(Schedule.objects.values_list('name', flat=True))
        expectations_list = list(Expectations.objects.values_list('name', flat=True))
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return Response({
            "specialization": specialization_list,
            "towns": towns_list,
            # salary
            "experience": experience_list,
            "education": education_list,
            "skills": skills_list,
            "languages": languages_list,
            "languages_levels": languages_levels_list,
            "registration": registration_list,
            "occupation": occupation_list,
            "timetable": timetable_list,
            "mission": MissionChoices.choices,
            "bonus": BonusChoices.choices,
            "expectations": expectations_list,
            "date": date,
            "recruiter_count": RECRUITER_COUNT_CHOICES,
            "candidates_count": CANDIDATES_COUNT_CHOICES,
            "payments": payments_list,
            # award
        })
