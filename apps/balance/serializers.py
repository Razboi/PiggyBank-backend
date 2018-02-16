from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
        "balance",
        "date",
        "description",
        "amount"
        ]
        read_only_fields = ["balance"]
