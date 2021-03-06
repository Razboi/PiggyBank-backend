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

class DeleteTransaction(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def delete(self, request):
        transaction = Transaction.objects.get(pk=request.data["pk"])
        balance = Balance.objects.get(pk=transaction.balance.pk)
        # we must undo the transaction on the balance before deleting it
        # if the amount was negative make it positive and add it
        if transaction.amount < 0:
            balance.totalBalance += -transaction.amount
        # else substract it
        else:
            balance.totalBalance -= transaction.amount
        balance.save()
        transaction.delete()
        return HttpResponse("Deleted")

class UpdateTransaction(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request):
        transaction = Transaction.objects.get(pk=request.data["pk"])
        balance = Balance.objects.get(pk=transaction.balance.pk)
        # if the amount has changed recalculate the balance
        # and recalculate the new currentTotal of the transaction
        if transaction.amount != request.data["amount"]:
            # if the old amount was negative make it positive and add it
            if transaction.amount < 0:
                balance.totalBalance += -transaction.amount
                new_trans_balance = transaction.currentTotal + -transaction.amount
            # else substract it
            else:
                balance.totalBalance -= transaction.amount
                new_trans_balance = transaction.currentTotal - transaction.amount
            # now we have removed the old amount on the totalBalance and we can
            # add the new amount
            balance.totalBalance += request.data["amount"]
            balance.save()
        # now we have the currentTotal before it was added the amount and we can
        # add the new amount
        new_trans_balance += request.data["amount"]
        # Using update() instead of save() avoids triggering the post_save method
        Transaction.objects.filter(pk=request.data["pk"]).update(
            description=request.data["description"],
            amount=request.data["amount"],
            currentTotal=new_trans_balance
        )

        return HttpResponse(transaction)

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
