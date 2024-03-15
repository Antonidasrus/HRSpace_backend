from rest_framework.serializers import ModelSerializer

from users.models import User
# from app.models import Comment, Follow, Group, Post, User
# from app_hr.models import Comment, Follow, Group, Post, User


class UserSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
