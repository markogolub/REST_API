from rest_framework import serializers
from account.models import Account


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