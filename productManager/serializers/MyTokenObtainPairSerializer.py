from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

  def validate(self, attrs):
    data = super().validate(attrs)

    user = self.user
    data['username'] = user.username

    # if user.is_superuser:
    #   raise serializers.ValidationError("Admins não podem fazer login aqui.")

    return data
