from rest_framework.serializers import ModelSerializer

# from users.models import User
from app.models import Application
# from app_hr.models import Comment, Follow, Group, Post, User


# class UserSerializer(ModelSerializer):

#     class Meta:
#         model = User
#         fields = '__all__'


class ApplicationSerializer(ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'


class Application2Serializer(ModelSerializer):

    class Meta:
        model = Application
        fields = ('employer_id', 'name', 'profession',)


class Application3Serializer(ModelSerializer):

    class Meta:
        model = Application
        if 1==2: # сюда принести слаг из урла
            fields = ('employer_id', 'name', 'profession',)
        if 1==1:
            fields = '__all__'
