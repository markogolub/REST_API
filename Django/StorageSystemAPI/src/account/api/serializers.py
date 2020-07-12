from rest_framework import serializers
from account.models import Account, Location


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = [
            'email',
            'username',
            'name',
            'surname',
            'phone',
            'cell_phone',
            'address',
            'residence',
            'data_joined',
            'last_login',
        ]


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Account
        fields = [
            'email',
            'username',
            'password',
            'password2',
            'name',
            'surname',
            'phone',
            'cell_phone',
            'address',
            'residence',
        ]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            name=self.validated_data['name'],
            surname=self.validated_data['surname'],
            phone=self.validated_data['phone'],
            cell_phone=self.validated_data['cell_phone'],
            address=self.validated_data['address'],
            residence=self.validated_data['residence'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})

        account.set_password(password)
        account.save()
        return account