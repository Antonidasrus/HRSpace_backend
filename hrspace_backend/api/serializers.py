from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from app.models import (Application,
                        Specialization,
                        Towns,
                        Skill,
                        Language,
                        Salaryrecomend,
                        LanguageApplication)


class SpecializationSerializer(ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'


class TownsSerializer(ModelSerializer):

    class Meta:
        model = Towns
        fields = '__all__'


# class SpecializationSerializer(ModelSerializer):
#     class Meta:
#         model = Specialization
#         fields = '__all__'

# class EducationSerializer(ModelSerializer):
#     class Meta:
#         model = Education
#         fields = '__all__'

# class PaymentsSerializer(ModelSerializer):
#     class Meta:
#         model = Payments
#         fields = '__all__'

class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

# class RegistrationSerializer(ModelSerializer):
#     class Meta:
#         model = Registration
#         fields = '__all__'

# class OccupationSerializer(ModelSerializer):
#     class Meta:
#         model = Occupation
#         fields = '__all__'

# class ScheduleSerializer(ModelSerializer):
#     class Meta:
#         model = Schedule
#         fields = '__all__'

# class ExpectationsSerializer(ModelSerializer):
#     class Meta:
#         model = Expectations
#         fields = '__all__'


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        # fields = '__all__'
        fields = ('name',)


class ApplicationSerializer(ModelSerializer):
    skills = serializers.StringRelatedField(many=True)
    specialization = serializers.StringRelatedField()
    experience = serializers.StringRelatedField()
    education = serializers.StringRelatedField()
    payments = serializers.StringRelatedField()
    towns = serializers.StringRelatedField()
    # languages = LanguageSerializer(many=True, source="language_list")
    languages = LanguageSerializer(many=True)
    towns = serializers.StringRelatedField()
    registration = serializers.StringRelatedField(many=True)
    occupation = serializers.StringRelatedField(many=True)
    timetable = serializers.StringRelatedField(many=True)
    expectations = serializers.StringRelatedField(many=True)

    class Meta:
        model = Application
        fields = '__all__'
        fields = ('id', 'employer_id', 'date', 'mission', 'bonus', 'salary_min', 'salary_max', 'responsibilities', 'other_requirements', 'candidates_count', 'recruiter_count', 'award', 'name', 'specialization', 'towns', 'experience', 'education', 'payments', 'skills', 'languages', 'registration', 'occupation', 'timetable', 'expectations')

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)

    #     languages = instance.languages.all()
    #     language_serializer = LanguageSerializer(languages, many=True)
    #     languages_data = language_serializer.data

    #     for language in language_serializer:
    #         language_level = LanguageApplication.objects.get(
    #             application_id=instance.id,
    #             language_id=language['id']).language_level
    #         language['language_level'] = language_level
    #     data['languages'] = languages_data

    #     return data


class SalarySerializer(ModelSerializer):

    class Meta:
        model = Salaryrecomend
        fields = ('id', 'salary_recomend')

