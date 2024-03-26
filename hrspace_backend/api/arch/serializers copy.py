from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

# from users.models import User
from app.models import Application
from app_hr.models import Application_hr

# class UserSerializer(ModelSerializer):

#     class Meta:
#         model = User
#         fields = '__all__'


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = "__all__"


class Application2Serializer(ModelSerializer):

    class Meta:
        model = Application
        fields = (
            "employer_id",
            "name",
            "profession",
        )


class Application3Serializer(ModelSerializer):

    class Meta:
        model = Application
        if 1 == 2:  # сюда принести слаг из урла
            fields = (
                "employer_id",
                "name",
                "profession",
            )
        if 1 == 1:
            fields = "__all__"


class Application4Serializer(ModelSerializer):

    class Meta:
        model = Application
        # fields = ('employer_id', 'name', 'profession', 'salary', 'created')
        fields = ("employer_id", "name", "profession", "created")
        # title_id = self.kwargs.get('profession_id')
        # if 1==2: # сюда принести слаг из урла
        #     fields = ('employer_id', 'name', 'profession',)
        # if 1==1:
        #     fields = '__all__'

    # def create(self, validated_data):
    #     request = self.context.get('request')
    #     application_id = request.parser_context['kwargs'].get('application_id')
    #     print('аааааааааааа')
    #     print(application_id)
    #     # if application_id == 2:
    #     if 2 == 2:
    #         print('ооооооооооо')
    #         self.fields['salary'] = serializers.IntegerField()
    #     return super().create(validated_data)

    def to_representation(self, instance):
        request = self.context.get("request")
        application_id = request.parser_context["kwargs"].get("application_id")
        if int(application_id) in [2, 4, 9]:
            print("ооооооооооо")
            self.fields["salary"] = serializers.IntegerField()
        return super().to_representation(instance)


"""
class Application_hrSerializer(ModelSerializer):

    class Meta:
        model = Application_hr
        fields = '__all__'
"""
