from rest_framework import serializers
from users.models import CustomUser
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only= False)
    email = serializers.EmailField(read_only= False)
    password = serializers.CharField(write_only= False)


    def create(self, validated_data):
        user = CustomUser(
            email = validated_data['email'],
            username= validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user= user)
        return user

    
    class Meta:
        model= CustomUser
        fields = ('username', 'password', 'email')