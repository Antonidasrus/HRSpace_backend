from rest_framework.serializers import ModelSerializer
from rest_framework import serializers, relations

from app.models import (Application,

                        Specialization,
                        Experience,
                        Education,
                        Payments,
                        Towns,

                        Skill,
                        Registration,
                        Occupation,
                        Schedule,
                        Expectations,

                        Language,
                        Salaryrecomend,
                        LanguageApplication
                        )


class SpecializationSerializer(ModelSerializer):

    class Meta:
        model = Specialization
        fields = '__all__'


class ExperienceSerializer(ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class EducationSerializer(ModelSerializer):
    class Meta:
        model = Education
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class PaymentsSerializer(ModelSerializer):
    class Meta:
        model = Payments
        fields = '__all__'


class TownsSerializer(ModelSerializer):

    class Meta:
        model = Towns
        fields = '__all__'
        # fields = ('name',)


class LanguageSerializer(ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

'''
class SpecializationSerializer(ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'


class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = Registration
        fields = '__all__'

class OccupationSerializer(ModelSerializer):
    class Meta:
        model = Occupation
        fields = '__all__'

class ScheduleSerializer(ModelSerializer):
    class Meta:
        model = Schedule
        fields = '__all__'

class ExpectationsSerializer(ModelSerializer):
    class Meta:
        model = Expectations
        fields = '__all__'

'''


class SkillSerializer(ModelSerializer):

    class Meta:
        model = Skill
        # fields = '__all__'
        fields = ('name',)


class ApplicationSerializer(ModelSerializer):
    specialization = serializers.CharField(source='specialization.name')
    experience = serializers.CharField(source='experience.name')
    education = serializers.CharField(source='education.name')
    payments = serializers.CharField(source='payments.name')
    towns = serializers.CharField(source='towns.name')

    # skills = SkillSerializer(many=True, source='skills_set')
    # skills = SkillSerializer(many=True, read_only=True)
    # skills = serializers.StringRelatedField(many=True)
    # skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(), many=True)
    skills = serializers.SlugRelatedField(
        queryset=Skill.objects.all(),
        slug_field='name',
        many=True
    )
    # registration = serializers.StringRelatedField(many=True)
    # occupation = serializers.StringRelatedField(many=True)
    # timetable = serializers.StringRelatedField(many=True)
    # expectations = serializers.StringRelatedField(many=True)

    # # languages = LanguageSerializer(many=True, source="language_list")
    # languages = LanguageSerializer(many=True)

    def create(self, validated_data):
        specialization_name = validated_data.pop('specialization', {}).get('name')
        experience_name = validated_data.pop('experience', {}).get('name')
        education_name = validated_data.pop('education', {}).get('name')
        payments_name = validated_data.pop('payments', {}).get('name')
        towns_name = validated_data.pop('towns', {}).get('name')

        skills_data = validated_data.pop('skills')

        specialization_instance, _ = Specialization.objects.get_or_create(name=specialization_name)
        experience_instance, _ = Experience.objects.get_or_create(name=experience_name)
        education_instance, _ = Education.objects.get_or_create(name=education_name)
        payments_instance, _ = Payments.objects.get_or_create(name=payments_name)
        towns_instance, _ = Towns.objects.get_or_create(name=towns_name)

        application = Application.objects.create(
            specialization=specialization_instance,
            experience=experience_instance,
            education=education_instance,
            payments=payments_instance,
            towns=towns_instance,
            **validated_data
        )
        application.skills.set(Skill.objects.filter(name__in=skills_data))
        return application

    class Meta:
        model = Application
        # fields = '__all__'
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
