from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializers(serializers.Serializer):
    id = serializers.ReadOnlyField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        intance = User()
        intance.first_name = validated_data.get('first_name')

        intance.last_name = validated_data.get('last_name')

        intance.username = validated_data.get('username')

        intance.email = validated_data.get('email')
        intance.set_password(validated_data.get('password'))

        intance.save()

    def validate_username(self, data):
        users = User.objects.filter(username=data)
        if len(users) !=0:
            raise serializers.ValidationError("Este nombre de usuario ya existe")
        else:
            return data