from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from app.models import (Application,
                        Specialization,
                        Towns,
                        Skill,
                        Language,
                        Salaryrecomend)


class SpecializationSerializer(ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'


class TownsSerializer(ModelSerializer):

    class Meta:
        model = Towns
        fields = '__all__'


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class LanguageSerializer(ModelSerializer):

    class Meta:
        model = Language
        fields = '__all__'


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'


class SalarySerializer(ModelSerializer):

    class Meta:
        model = Salaryrecomend
        fields = ('id', 'salary_recomend')

#     def to_representation(self, instance):
#         queryset = self.instance
#         total_salary = sum(salary.salary_recomend for salary in queryset)
#         average_salary = total_salary / queryset.count() if queryset.count() > 0 else 0
#         if isinstance(queryset, list) and len(queryset) > 0:
#             return [{'average_salary_recomend': average_salary}]
#         return {'average_salary_recomend': average_salary}


class AverageSalarySerializer(serializers.Serializer):
    average_salary_recomend = serializers.DecimalField(max_digits=10, decimal_places=2)
