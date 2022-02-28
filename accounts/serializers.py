from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    re_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'is_renter', 'password', 're_password')
        extra_kwargs = {'password': {'write_only': True}, 're_password': {'write_only': True}, 'is_renter': {'read_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['re_password']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'], name=validated_data['name'], password=validated_data['password'])
        return user


class BasicUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')
        extra_kwargs = {'name': {'read_only': True}, 'email': {'read_only': True}}
