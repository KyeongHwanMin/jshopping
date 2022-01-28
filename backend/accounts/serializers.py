from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # 쓰기전용

    def create(self, validated_data): # validation이 유효할 때 저장
        user = User.objects.create(username=validated_data["username"])
        user.set_password(validated_data["password"]) # 암호화 해서 저장
        user.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'password'] # password를 직접 넣게되면 값이 보이게 됨.