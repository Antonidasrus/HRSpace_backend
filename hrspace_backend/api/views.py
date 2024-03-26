from datetime import datetime

from django.db.models import Avg
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from app.models import (BOOLEAN_CHOICES, CANDIDATES_COUNT_CHOICES,
                        PAYMENTS_CHOICES, RECRUITER_COUNT_CHOICES, Application,
                        Education, Expectations, Experience, Language,
                        LanguageLevel, Occupation, Payments, Registration,
                        Salaryrecomend, Schedule, Skill, Specialization, Towns)

from .serializers import (ApplicationSerializer, LanguageSerializer,
                          SalarySerializer, SkillSerializer,
                          SpecializationSerializer, TownsSerializer)
from .utils import istartswith_search


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="Specializations-get",
        operation_description="Получаем специализацию",
        tags=["Specialization"],
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Specializations-get-list",
        operation_description="Получаем список специализаций",
        tags=["Specialization"],
    ),
)
class SpecializationViewSet(ReadOnlyModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="Towns-get",
        operation_description="Получаем город",
        tags=["Towns"]
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Towns-get-list",
        operation_description="Получаем список городов",
        tags=["Towns"],
    ),
)
class TownsViewSet(ReadOnlyModelViewSet):
    queryset = Towns.objects.all()
    serializer_class = TownsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="Language-get",
        operation_description="Получаем знание языков",
        tags=["Language"],
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Language-get-list",
        operation_description="Получаем список знаний языков",
        tags=["Language"],
    ),
)
class LanguageViewSet(ReadOnlyModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        return istartswith_search(queryset, self)


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="Skill-get",
        operation_description="Получаем навык",
        tags=["Skill"]
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Skill-get-list",
        operation_description="Получаем список навыков",
        tags=["Skill"],
    ),
)
class SkillViewSet(ReadOnlyModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_name = self.request.query_params.get(
            "specialization_name"
        )
        if specialization_name:
            queryset = queryset.filter(
                specialization__name=specialization_name
            )
        return istartswith_search(queryset, self)


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="Salary-get",
        operation_description="Получаем рекомендуемую зарплату",
        tags=["Salary"],
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Salary-get-list",
        operation_description="Получаем список рекомендуемой зарплаты",
        tags=["Salary"],
    ),
)
class SalaryViewSet(ReadOnlyModelViewSet):
    queryset = Salaryrecomend.objects.all()
    serializer_class = SalarySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        specialization_name = self.request.query_params.get(
            "specialization_name"
        )
        if specialization_name:
            queryset = queryset.filter(
                specialization__name=specialization_name
            )
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(
                salaryrecomendtown__town_id__name__istartswith=name
            )
        average_salary = queryset.aggregate(average_salary=Avg(
            "salary_recomend"
        ))["average_salary"]
        created_salary_recomend = Salaryrecomend(
            salary_recomend=average_salary
        )
        return [created_salary_recomend]


@method_decorator(
    name="retrieve",
    decorator=swagger_auto_schema(
        operation_id="Application-get",
        operation_description="Получаем заявку",
        tags=["Application"],
    ),
)
@method_decorator(
    name="list",
    decorator=swagger_auto_schema(
        operation_id="Application-get-list",
        operation_description="Получаем список заявок",
        tags=["Application"],
    ),
)
@method_decorator(
    name="create",
    decorator=swagger_auto_schema(
        operation_id="Application-post",
        operation_description="Создаем заявку",
        tags=["Application"],
    ),
)
@method_decorator(
    name="update",
    decorator=swagger_auto_schema(
        operation_id="Application-put",
        operation_description="Обновляем всю заявку",
        tags=["Application"],
    ),
)
@method_decorator(
    name="partial_update",
    decorator=swagger_auto_schema(
        operation_id="Application-patch",
        operation_description="Обновляем заявку",
        tags=["Application"],
    ),
)
@method_decorator(
    name="destroy",
    decorator=swagger_auto_schema(
        operation_id="Application-delete",
        operation_description="Удаляем заявку",
        tags=["Application"],
    ),
)
class ApplicationViewSet(ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class AllData(APIView):
    @swagger_auto_schema(
        operation_id="All-get-list",
        operation_description="Получаем список",
        tags=["All"],
    )
    def get(self, request):
        skills_list = list(
            Skill.objects.values_list(
                "name", flat=True).order_by('name')
        )
        specialization_list = list(
            Specialization.objects.values_list(
                "name", flat=True).order_by('name')
        )
        experience_list = list(
            Experience.objects.values_list(
                "name", flat=True).order_by('name')
        )
        education_list = list(
            Education.objects.values_list(
                "name", flat=True).order_by('name')
        )
        towns_list = list(
            Towns.objects.values_list(
                "name", flat=True).order_by('name')
        )
        languages_list = list(
            Language.objects.values_list(
                "name", flat=True).order_by('name')
        )
        languages_levels_list = list(
            LanguageLevel.objects.values_list(
                "name", flat=True).order_by('name')
        )
        registration_list = list(
            Registration.objects.values_list(
                "name", flat=True).order_by('name')
        )
        occupation_list = list(
            Occupation.objects.values_list(
                "name", flat=True).order_by('name')
        )
        timetable_list = list(
            Schedule.objects.values_list(
                "name", flat=True).order_by('name')
        )
        expectations_list = list(
            Expectations.objects.values_list(
                "name", flat=True).order_by('name')
        )
        payments_list = list(
            Payments.objects.values_list(
                "name", flat=True).order_by('id')
        )
        date = datetime.now().strftime("%Y-%m-%d")

        return Response(
            {
                "specialization": specialization_list,
                "towns": towns_list,
                "experience": experience_list,
                "education": education_list,
                "skills": skills_list,
                "languages": languages_list,
                "languages_levels": languages_levels_list,
                "registration": registration_list,
                "occupation": occupation_list,
                "timetable": timetable_list,
                "mission": BOOLEAN_CHOICES,
                "bonus": BOOLEAN_CHOICES,
                "expectations": expectations_list,
                "date": date,
                "recruiter_count": RECRUITER_COUNT_CHOICES,
                "candidates_count": CANDIDATES_COUNT_CHOICES,
                # "payments": PAYMENTS_CHOICES,
                "payments": payments_list
            }
        )
