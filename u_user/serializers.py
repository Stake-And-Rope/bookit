from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from u_user.models import User

class UserSerializer(serializers.ModelSerializer):
    # first_name = serializers.CharField(max_length = 50)
    # last_name = serializers.CharField(max_length = 50)
    # email = serializers.EmailField(
    #         required=True,
    #         validators=[UniqueValidator(queryset=User.objects.all())]
    #         )
    # username = serializers.CharField(
    #         validators=[UniqueValidator(queryset=User.objects.all())]
    #         )
    # password = serializers.CharField(min_length=8)

    # def create(self, validated_data):
    #     user = User.objects.create_user(validated_data['username'], validated_data['email'],
    #          validated_data['password'])
    #     return user

    class Meta:
        model = User
        fields = '__all__'