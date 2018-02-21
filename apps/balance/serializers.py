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
        "currentTotal"
        ]
        read_only_fields = ["balance"]

class CurrentBalanceSerializer(serializers.Serializer):
    totalBalance = serializers.DecimalField(decimal_places=2, max_digits=20)
