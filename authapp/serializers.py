from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=CustomUser.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'password')