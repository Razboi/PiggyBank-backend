from rest_framework import generics, mixins, authentication, permissions
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import TransactionSerializer, CurrentBalanceSerializer
from .models import Transaction, Balance
from ..users.models import Account
from rest_framework.fields import CurrentUserDefault
from django.http import HttpResponse
import json


class CreateTransaction(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        account = Account.objects.get(user=request.user)
        balance = Balance.objects.get(user=account)
        new_transaction = Transaction(
        balance=balance,
        description=request.data["description"],
        amount=request.data["amount"]
        )
        new_transaction.save()
        return HttpResponse(new_transaction)

class AllTransactionsView(generics.ListAPIView):
    lookup_field = "pk"
    serializer_class = TransactionSerializer

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        balance = Balance.objects.get(user=account)
        qs = Transaction.objects.filter(balance=balance).order_by("-date")
        return qs

class TransactionsCreateView(generics.ListAPIView):
    lookup_field = "pk"
    serializer_class = TransactionSerializer

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        balance = Balance.objects.get(user=account)
        qs = Transaction.objects.filter(balance=balance).order_by("-date")[:10]
        return qs

class BalanceRetrieveView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        account = Account.objects.get(user=request.user)
        balance = Balance.objects.get(user=account)
        serializer = CurrentBalanceSerializer(balance)
        return Response(serializer.data)
