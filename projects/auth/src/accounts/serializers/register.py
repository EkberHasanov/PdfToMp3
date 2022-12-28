from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework import serializers

from accounts.models import User

UserModel = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2',)

    def validate(self, attrs: dict) -> dict:
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Passwords didn't match"})
        return attrs

    def create(self, validated_data: dict) -> User:
        user = UserModel.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password1'])
        user.save()

        return user
