from accounts.models import Account
from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class TransactionSerializer:
    def __init__(self, account):
        self.data = None
        self.account = account

class AccountSerializer(serializers.ModelSerializer):
    bank_code_display = serializers.CharField(source='get_bank_code_display', read_only=True)
    type_display = serializers.CharField(source='get_type_display', read_only=True)

    class Meta:
        model = Account
        fields = [
            'id', 'account_number', 'bank_code', 'bank_code_display',
            'type', 'type_display', 'balance'
        ]