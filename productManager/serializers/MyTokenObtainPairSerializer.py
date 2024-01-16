from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  def validate(self, attrs):
    data = super().validate(attrs)
  
    data['username'] = self.user.username
    
    user = self.user
    if user.is_admin:
        raise serializers.ValidationError("Admins não podem fazer login aqui.")

    return data