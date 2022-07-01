from accounts.models import User, UserProfile
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'first_name',
            'last_name',
            'username',
            'balance_amount',
            'email',
            'password',
        ]
        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data.update({
            "balance_amount": instance.get_balance_amount,
        })
        return data


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        exclude = ('user', )
