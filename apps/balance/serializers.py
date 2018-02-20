from rest_framework import serializers
from .models import Transaction, Balance

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
        "balance",
        "date",
        "description",
        "amount",
        "transaction_balance"
        ]
        read_only_fields = ["balance"]
