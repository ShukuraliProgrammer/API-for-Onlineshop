from accounts.models import BaseUser, Profile, Address
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = BaseUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )
        return user

    class Meta:
        model = BaseUser
        fields = ('password', 'username', 'first_name', 'last_name',)
        extra_kwargs = {'password': {'write_only': True, 'min_length': 8}}


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'name', 'photo', 'phone', 'description', 'gender', 'birth_date')
        extra_kwargs = {'phone': {'read_only': True, 'max_length': 13}}

    # def create(self, validated_data):
    #     user_data = validated_data.pop("user")
    #     user_serializer = UserSerializer(data=user_data)
    #     if user_serializer.is_valid():
    #         user = user_serializer.save()
    #         profile_serializer = ProfileSerializer(data=validated_data)
    #         if profile_serializer.is_valid():
    #             profile = profile_serializer.save(user=user)
    #             return profile
    #         else:
    #             print(profile_serializer.errors)
    #     else:
    #         print(user_serializer.errors)
    #     return None


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('profile', 'region', 'city', 'district', 'state', 'address', 'date_created')

