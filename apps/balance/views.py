from rest_framework import generics, mixins, authentication, permissions
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import TransactionSerializer, CurrentBalanceSerializer
from .models import Transaction, Balance
from ..users.models import Account
from rest_framework.fields import CurrentUserDefault

class TransactionsCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "pk"
    serializer_class = TransactionSerializer

    def get_queryset(self):
        account = Account.objects.get(user=self.request.user)
        balance = Balance.objects.get(user=account)
        qs = Transaction.objects.filter(balance=balance)
        return qs

    def perform_create(self, serializer):
        account = Account.objects.get(user=self.request.user)
        balance = Balance.objects.get(user=account)
        serializer.save(balance=balance)

# using mixins to add the post method on the listAPIview
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class BalanceRetrieveView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        account = Account.objects.get(user=request.user)
        balance = Balance.objects.get(user=account)
        serializer = CurrentBalanceSerializer(balance)
        return Response(serializer.data)
